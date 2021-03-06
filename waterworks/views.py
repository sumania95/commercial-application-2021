from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
)

#functions
from django.db.models.functions import Coalesce,Concat
from django.db.models import Q,F,Sum,Count
from django.db.models import Value
from django.urls import reverse
#datetime
from datetime import datetime
#JSON AJAX
from django.template.loader import render_to_string
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin


class Waterworks_Home(TemplateView):
    template_name = 'waterworks/pages/dashboard.html'

class Waterworks_Profile(TemplateView):
    template_name = 'waterworks/pages/profile.html'

class Waterworks_Reading(TemplateView):
    template_name = 'waterworks/pages/reading.html'

class Waterworks_Billing_Period(TemplateView):
    template_name = 'waterworks/pages/billing_period.html'

class Waterworks_Barangay(TemplateView):
    template_name = 'waterworks/pages/barangay.html'

class Waterworks_Accounts(TemplateView):
    template_name = 'waterworks/pages/accounts.html'
