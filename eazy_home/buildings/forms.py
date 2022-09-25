from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddBuildingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Building
        fields = ['number', 'street', 'city', 'type_object']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-input'}),
        #     'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        # }

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title) > 200:
    #         raise ValidationError('Длина превышает 200 символов')
    #
    #     return title

class AddFlatsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['building_id'].empty_label = "Дом не выбран"

    class Meta:
        model = Flat_table
        fields = ['flat_id', 'number', 'entrance', 'floor', 'area', 'live_area', 'room_count', 'price', 'type_object']
        # building = models.ForeignKey(Building, on_delete=models.CASCADE)
