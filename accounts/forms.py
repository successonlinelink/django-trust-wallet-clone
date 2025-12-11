from userauths.models import Profile
from django import forms
# from bootstrap_datepicker_plus import DatePickerInput


class DateInput(forms.DateInput):
    input_type = 'date'

class ProfileUpdateForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Full Name"}), required=True)
    
    image = forms.ImageField(widget=forms.FileInput(attrs={"class":""}), required=True)
    identity_image = forms.ImageField(widget=forms.FileInput(attrs={"class":""}), required=True)
    current_address = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Current Address", "class":""}), required=True)
    country = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Country", "class":""}), required=True)
    state = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "State", "class":""}), required=True)
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "City", "class":""}), required=True)
    mobile = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': "Mobile", "class":""}), required=True)
    fax = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': "Fax", "class":""}), required=True)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Date of Birth', 'class': ''}), input_formats=['%Y-%m-%d'], required=True)

    class Meta:
        model = Profile
        fields = [
            'full_name',
            'image',
            'country',
            'state',
            'city',
            'mobile',
            'fax',
            'current_address',
            'gender',
            'date_of_birth',
            'marrital_status',
            'identity_type',
            'identity_image',
        ]

    # this guy will apply automatic class to all the fields with class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = "tf-select" # and the is the border around the input
