
from django import forms
from django.contrib.auth.models import User
from core.models import Technology, UserTechStack



# Form for Registering
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        # Add class and placeholder to form fields
        widgets = {
            'username': forms.TextInput(attrs={'class':'input-field','placeholder':'Username'}),
            'email': forms.TextInput(attrs={'class':'input-field','placeholder':'Email'}),
            'password': forms.TextInput(attrs={'class':'input-field','placeholder':'Password'}),
        }


# Form for adding/updating new record
class TechStackForm(forms.ModelForm):
    class Meta:
        model = UserTechStack
        fields = ['category', 'technology', 'expertise_level','learning_resource']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add class and placeholder to form fields
        self.fields['category'].widget.attrs = {'class':'form-control', 'id':'id_category', 'name':'category'}
        self.fields['technology'].widget.attrs = {'class':'form-control', 'id':'id_technology', 'name':'technology'}
        self.fields['expertise_level'].widget.attrs = {'class':'form-control', 'id':'id_expertise_level', 'name':'expertise_level'}
        self.fields['learning_resource'].widget.attrs = {'class':'form-control', 'id':'id_learning_resource', 'name':'learning_resource'}
        # By default technology dropdown is set to null
        self.fields['technology'].queryset = Technology.objects.none()
        
        if 'category' in self.data:
            try:
                # Get technologies under category
                category_id = int(self.data.get('category'))
                self.fields['technology'].queryset = Technology.objects.filter(category__id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['technology'].queryset = self.instance.category.technology_set.order_by('name')
