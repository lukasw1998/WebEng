from django import forms
import datetime

class NoticeForm(forms.Form):
    date_formats = ['%d.%m.%Y', '%d.%m.%y']
    title = forms.CharField(label='Titel', max_length=80)
    text = forms.CharField(label='Text', max_length=400)
    start = forms.DateField(label='Von',
                            input_formats=date_formats,
                            initial=datetime.date.today)
    end = forms.DateField(label='Bis',
                          input_formats=date_formats,
                          initial=datetime.date.today)