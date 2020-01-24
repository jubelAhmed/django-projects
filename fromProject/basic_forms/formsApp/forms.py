from django import forms
from django.core import validators

def check_all_character(value):
    
    v = value.replace(' ','')
    #check all value is alphabet not allow number or speical character
    if not v.isalpha():
        raise forms.ValidationError("All characher must be alphabet")
        

class FormName(forms.Form):
    name = forms.CharField(validators=[check_all_character])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    
    ## no need this beacuse django have default validator
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
        
    #     if(len(botcatcher)>0):
    #         raise forms.ValidationError("GOTCHA BOT ! ")
    #     return botcatcher
        


    #
    ## use clean() method for auto call and get all data
    
    ## check correct email 
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']
        
        if email != v_email :
            raise forms.ValidationError("Make sure email match!")
    