import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import widgets
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, View, TemplateView
from django.views.generic.edit import CreateView, UpdateView


from .models import Student


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "list.html"
    paginate_by = 15

    def test_func(self):
        return self.request.user.is_active

    def get_context_data(self, **kwargs):
        qs = self.model.objects.all().order_by('-pk')
        
        kwargs['count'] = qs.count()
        return super().get_context_data(**kwargs)

    template_name = "list.html"


# class StudentDetailView(LoginRequiredMixin, DetailView):
#     model = Student
#     template_name = "students/student_detail.html"

#     def get_context_data(self, **kwargs):
#         context = super(StudentDetailView, self).get_context_data(**kwargs)
#         context["payments"] = Invoice.objects.filter(student=self.object)
#         return context

class StudentDashboard(
    LoginRequiredMixin,
    TemplateView
):
    """Student Dashboard view"""
    template_name = 'student_dashboard.html'

    def test_func(self):
        return self.request.user.is_active

class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Student
    fields = "__all__"
    template_name = 'create.html'
    success_message = "New student successfully added."

    def get_form(self):
        form = super(StudentCreateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 2})
        return form


class StudentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Student
    fields = "__all__"
    success_message = "Record successfully updated."

    def get_form(self):
        """add date picker in forms"""
        form = super(StudentUpdateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["date_of_admission"].widget = widgets.DateInput(
            attrs={"type": "date"}
        )
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 2})
        form.fields['passport'].widget = widgets.FileInput()
        return form


# class StudentDeleteView(LoginRequiredMixin, DeleteView):
#     model = Student
#     success_url = reverse_lazy("student-list")


# class StudentBulkUploadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#     model = StudentBulkUpload
#     template_name = "students/students_upload.html"
#     fields = ["csv_file"]
#     success_url = "/student/list"
#     success_message = "Successfully uploaded students"


class DownloadCSVViewdownloadcsv(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="student_template.csv"'

        writer = csv.writer(response)
        writer.writerow(
            [
                "registration_number",
                "surname",
                "firstname",
                "other_names",
                "gender",
                "parent_number",
                "address",
                "current_class",
            ]
        )

        return response
