from django.views.generic import *
from firebase.utils.firebase_config import *
from firebase.utils.constants import Templates, Constants
from firebase.forms import Employee
from django.urls import reverse_lazy
from firebase.utils.constants import Urls
from time import time
from math import floor
from django.http import HttpResponseRedirect
from django.contrib.messages import info

# def home(request):
# 	day = database.child('Data').child('Day').get().val()
# 	id = database.child('Data').child('ID').get().val()
# 	projectname = database.child('Data').child('Project').get().val()
# 	return render(request,"home.html",{"day":day,"id":id,"projectname":projectname })


class HomeView(TemplateView):
    template_name = Templates.HOME.value

    def dispatch(self, request, *args, **kwargs):
        if self.request.session.get("uid") is None:
            info(request, Constants.NOT_AUTHENTICATED.value)
            return HttpResponseRedirect(reverse_lazy(Urls.LOGIN_REVERSE.value))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = database.child("Employees").get().val()
        context["employees"] = []
        for key, value in data.items():
            context["employees"].append(value)
        return context


class AddEmployeeView(FormView):
    template_name = Templates.ADD.value
    form_class = Employee
    success_url = reverse_lazy(Urls.HOME_REVERSE.value)

    def dispatch(self, request, *args, **kwargs):
        if self.request.session.get("uid") is None:
            info(request, Constants.NOT_AUTHENTICATED.value)
            return HttpResponseRedirect(reverse_lazy(Urls.LOGIN_REVERSE.value))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        try:
            uid = self.request.session.get("uid")
            user = auth.get_account_info(uid)
            print(user)
            data = form.cleaned_data
            database.child("Employees").child(floor(time())).set(
                data, json_kwargs={"indent": 4, "sort_keys": True, "default": str}
            )
            return super().form_valid(form)
        except Exception as err:
            form.add_error(None, err)
            return super().form_invalid(form)
