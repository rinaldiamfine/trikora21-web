from django import forms
from django.contrib.auth import authenticate, login, get_user_model
# from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()
from .models import Profile
# from global_data.models import Template, Language

GENDER_CHOICES = (
    ('n', 'Not Selected'),
	('m', 'Male'),
	('f', 'Female'),
)
class ProfileForm(forms.ModelForm):
    # template    = forms.ModelChoiceField(queryset=Template.objects.all(), empty_label="Select Template")
    gender      = forms.ChoiceField(widget=forms.Select(), choices=GENDER_CHOICES)
    # language    = forms.ModelMultipleChoiceField(queryset=Language.objects.all())

    class Meta:
        model = Profile
        # fields = '__all__'
        fields = [
            'name', 'title', 'phone', 'email', 
            # 'template',
            'birthday',
            'gender',
            # 'languages',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Name'}),
            'title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Title'}),
            'phone': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Phone'}),
            'email': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            # 'bio': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Bio', 'style': 'height:100px;'}),
            'birthday': forms.DateInput(attrs={'class': 'input is-hidden is-calendar', 'placeholder': 'Birthday', 'type':'date'},),
            
        }

class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'username','password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class LoginForm(forms.Form):
    email    = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        request = self.request
        data = self.cleaned_data
        email  = data.get("email")
        password  = data.get("password")
        qs = User.objects.filter(email=email)
        if qs.exists():
            # user email is registered, check active/
            not_active = qs.filter(active=False)
            if not_active.exists():
                ## not active, check email activation
                link = reverse("account:resend-activation")
                reconfirm_msg = """Go to <a href='{resend_link}'>
                resend confirmation email</a>.
                """.format(resend_link = link)
                confirm_email = EmailActivation.objects.filter(email=email)
                is_confirmable = confirm_email.confirmable().exists()
                if is_confirmable:
                    msg1 = "Please check your email to confirm your account or " + reconfirm_msg.lower()
                    raise forms.ValidationError(mark_safe(msg1))
                email_confirm_exists = EmailActivation.objects.email_exists(email).exists()
                if email_confirm_exists:
                    msg2 = "Email not confirmed. " + reconfirm_msg
                    raise forms.ValidationError(mark_safe(msg2))
                if not is_confirmable and not email_confirm_exists:
                    raise forms.ValidationError("This user is inactive.")
        user = authenticate(request, username=email, password=password)
        if user is None:
            raise forms.ValidationError("Invalid credentials")
        login(request, user)
        self.user = user
        return data