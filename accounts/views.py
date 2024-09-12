from django.views.generic import *
from accounts.utils.constants import Templates, SuccessMessages, ErrorMessages
from accounts.forms import UserLoginForm, UserRegisterForm
from firebase.utils.firebase_config import *
from requests.exceptions import HTTPError
from django.contrib.messages import info
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect


class LoginView(FormView):
    template_name = Templates.SIGN_IN.value
    form_class = UserLoginForm
    success_url = "/"

    def form_valid(self, form):
        from pprint import pp

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        print(email, password)
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session_id = user.get("idToken")
            self.request.session["uid"] = session_id
            pp(self.request.session.__dict__)

            info(self.request, SuccessMessages.LOGIN.value)
            return super().form_valid(form)
        except HTTPError:
            form.add_error(None, ErrorMessages.LOGIN.value)
            return super().form_invalid(form)
        except Exception as err:
            print(f"Other error occurred: {err}")
            form.add_error(None, err)
            return super().form_invalid(form)


class RegisterView(FormView):
    template_name = Templates.REGISTER.value
    form_class = UserRegisterForm
    success_url = "/accounts/login/"

    def form_valid(self, form):
        try:
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = auth.create_user_with_email_and_password(email, password)
            data = {"name": name, "status": 1}
            uid = user.get("localId")
            database.child("users").child(uid).child("details").set(data)
            info(self.request, SuccessMessages.SIGNUP.value)
            return super().form_valid(form)
        except Exception as err:
            from pprint import pp

            pp(err.__dict__)
            form.add_error(None, f"Other error occurred: {err}")
            return super().form_invalid(form)


class LogOutView(View):
    def get(self, request):
        logout(request)
        print(request.session.__dict__)
        info(request, SuccessMessages.LOGOUT.value)
        return redirect("/accounts/login/")
