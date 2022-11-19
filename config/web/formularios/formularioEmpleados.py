from django import forms

class FormularioEmpleados(forms.Form):
    CARGO=(
        (1, 'Chef'),
        (2, 'Administrador'),
        (3, 'Mesero'),
        (4, 'Ayudante')
    )

    nombre=forms.CharField(
        #required=True,
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    apellido=forms.CharField(
        #required=True,
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}),
    )
    imagen=forms.CharField(
        #required=True,
        widget=forms.Textarea(attrs={'class': 'form-control mb-3'}),
    )
    cargo=forms.ChoiceField(
        #required=True,
        widget=forms.Select(attrs={'class': 'form-control mb-3'}),
        choices=CARGO
    )
    salario=forms.CharField(
        #required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class': 'form-control mb-3'}),
    )
    telefono=forms.CharField(
        #required=True,
        label='Contacto telefono',
        widget=forms.NumberInput(attrs={'class': 'form-control mb-3 '}),
    )
    email=forms.CharField(
        #required=True,
        label='Contacto email',
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )