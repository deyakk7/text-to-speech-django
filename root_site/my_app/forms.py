from django import forms


from .models import Storage

class InputForm(forms.ModelForm):
    class Meta:
        model = Storage
        exclude = ('audio', 'created_at', 'slug', 'title_small')
        widgets = {
            'title': forms.TextInput(attrs={
                "class": 'form-control',
                "placeholder": "Введіть назву",
            }),
            'text': forms.Textarea(attrs={
                "class": 'form-control',
                "placeholder": "Введіть текст",
                "rows": 8,
                
            }),
            'lang': forms.Select(attrs={
                "class": 'form-control',
            }),
        }
        labels = {
            'title': 'Назва до цього тексту',
            'text': 'Ваш текст',
            'lang': 'Мова',
        }

        error_messages = {
            'title': {
                'required': 'Це поле обов\'язкове',
                'max_length': 'Максимальна довжина 100 символів',
                'unique': 'Така назва вже існує, введіть іншу',
            },
            'text': {
                'required': 'Це поле обов\'язкове',
            },
            'lang': {
                'required': 'Це поле обов\'язкове',
            },
        }