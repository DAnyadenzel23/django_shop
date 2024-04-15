from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(20, 201, 20)]


class CartAddSectionForm(forms.Form):
    quantity = forms.IntegerField(max_value=500, label='')
    exclude = ['quantity']
    #quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='кг   ')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class CartUpdateSectionForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label=False)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)