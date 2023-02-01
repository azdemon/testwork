# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.http.response import HttpResponse
from django.views.generic.edit import FormView
from django.shortcuts import redirect, render
from .tasks import send_emails
from .forms import SendEmailForm
# from PIL import Image

class SensEmailsView(FormView):
    template_name = 'emailer/index.html'
    form_class = SendEmailForm

    def form_valid(self, form):
        send_emails.delay()
        return redirect('/success')
        
        
def success(request):
    return render(request, "emailer/success.html")

# def image_load(request):
#     print("\nImage Loaded\n")
#     red = Image.new('RGB', (1, 1))
#     response = HttpResponse(content_type="image/png")
#     red.save(response, "PNG")
#     return response