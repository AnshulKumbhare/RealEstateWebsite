from django import forms
from shelter_app.models import shelterproperties

class ShelterPropertiesForm(forms.ModelForm):

    
    class Meta:
        model = shelterproperties
        fields = '__all__'
        widgets = {
            'firstname' : forms.TextInput(attrs={'style':'margin:20px; width:80%;', 'id':'sp-inp', 'placeholder':'Enter First Name'}),
            'middlename': forms.TextInput(attrs={'style':'margin:20px;  width:80%; ', 'id': 'sp-inp', 'placeholder':'Enter Middle Name'}),
            'lastname': forms.TextInput(attrs={'style':'margin:20px;  width:80%;', 'id': 'sp-inp', 'placeholder':'Enter Last Name'}),
            'email': forms.EmailInput(attrs={'style':'margin:20px; width: 80%;', 'id': 'sp-inp', 'placeholder':'Enter Email'}),
            'mob1': forms.NumberInput(attrs={'style':'margin:20px; width:80%;', 'id': 'sp-inp', 'placeholder':'Enter Mobile 1'}),
            'mob2': forms.NumberInput(attrs={'style':'margin:20px; width:80%;', 'id': 'sp-inp', 'placeholder':'Enter Mobile 2'}),
            'address': forms.Textarea(attrs={'style':'margin:20px; width:95%;', 'id': 'sp-inp', 'placeholder':'Enter Address', 'rows':'5'}),
            'city': forms.TextInput(attrs={'style':'margin:20px; width: 60%', 'id': 'sp-inp', 'placeholder':'Enter City'}),
            'propertyname': forms.TextInput(attrs={'style':'margin:20px; width: 70%', 'id': 'sp-inp', 'placeholder':'Enter Property Name'}),
            'ptype1': forms.Select(attrs={'style':'margin:20px; width: 150px', 'id': 'sp-inp', 'placeholder':'Enter City'}),
            'ptype2': forms.Select(attrs={'style':'margin:20px; width: 150px', 'id': 'sp-inp', 'placeholder':'Enter City'}),
            'beds': forms.NumberInput(attrs={'style':'margin:20px; width: 200px', 'id': 'sp-inp', 'placeholder':'Enter Number of Beds'}),
            'area': forms.NumberInput(attrs={'style':'margin:20px; width: 200px', 'id': 'sp-inp', 'placeholder':'Enter Area (in sqft)'}),
            'price': forms.NumberInput(attrs={'style':'margin:20px; width: 60%', 'id': 'sp-inp', 'placeholder':'Enter Price (in Rs)'}),     
            'description': forms.Textarea(attrs={'style':'margin:20px; width: 95%', 'id': 'sp-inp', 'placeholder':'Describe your property (in not more than 120 Charecters)', 'rows':'5'}),   
            'pimage':forms.FileInput(attrs={'style':'margin:20px; color: red;'})
        }