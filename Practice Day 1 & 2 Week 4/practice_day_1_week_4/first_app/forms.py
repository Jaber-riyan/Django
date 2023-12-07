from django import forms
import datetime

class FormExample(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    check = forms.BooleanField()
    date = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years='BIRTH_YEAR_CHOICES'))
    value = forms.DecimalField()
    massage = forms.CharField(max_length=20)
    email = forms.CharField(label='Please enter your valid email address')
    your_name = forms.CharField(initial='Your name')
    agree = forms.BooleanField(initial=True)
    day = forms.DateField(initial=datetime.date.today)
    CHOICE = [
        ('blue','Blue'),
        ('skyblue','SkyBlue'),
        ('black','Black'),
        ('white','White'),
    ]
    color_choice = forms.ChoiceField(choices=CHOICE)
    color_choice_radio = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICE)
    color_choice_multiple_select = forms.MultipleChoiceField(choices=CHOICE)
    color_choice_multiple_auto = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=CHOICE)