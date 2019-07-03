from django.shortcuts import render
from django.views.generic import View
from .forms import FetchParentForm


class FetchParentView(View):
    form_class = FetchParentForm
    template_name = 'fetchparent.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            fetch_request = form.save()
        return render(request, self.template_name, {'form': form})

