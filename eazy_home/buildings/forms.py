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

# class AddFlatsForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         #self.fields['building'].empty_label = "Дом не выбран"
#     class Meta:
#         model = Flat
#         building = forms.ModelChoiceField(queryset=Building.objects.distinct('street'))
#         fields = ['number', 'entrance', 'floor', 'area', 'live_area', 'room_count', 'price', 'type_object']

class AddDealForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Deal
        fields = ['id_status_deal', 'id_type_deal']

class AddContractForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Contract
        fields = ['contractnumber', 'sum', 'id_deal', 'description']

class AddEstateForm(forms.ModelForm):
    class Meta:
        model = Estate
        fields = ['address', 'active', 'type_object']

class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['firstname', 'lastname', 'email', 'telephone']


