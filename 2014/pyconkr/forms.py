from django import forms


class EmailLoginForm(forms.Form):
    email = forms.EmailField(
        max_length=255,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Email address',
            'class': 'form-control',
        })
    )

    def clean(self):
        cleaned_data = super(EmailLoginForm, self).clean()
        return cleaned_data
