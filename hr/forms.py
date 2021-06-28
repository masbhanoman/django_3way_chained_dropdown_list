from django import forms
from .models import Person, City, Vanue

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'birthdate', 'country', 'city', 'vanue')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['city'].queryset = City.objects.none()

        

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')

        self.fields['vanue'].queryset = City.objects.none()
        if 'city' in self.data:
            try:
                city_id = int(self.data.get('city'))
                self.fields['vanue'].queryset = Vanue.objects.filter(city_id=city_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            #self.fields['vanue'].queryset = self.instance.country.city.vanue_set.order_by('name')
            self.fields['vanue'].queryset = self.instance.city.vanue_set.order_by('name')
