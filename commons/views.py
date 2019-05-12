from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "commons/dashboard.html"
    redirect_field_name = 'redirect_to'
    login_url = 'login'
