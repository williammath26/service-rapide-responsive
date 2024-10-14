from django import forms
from .models import solicitar, recuperacao

class SolicitarForm(forms.ModelForm):
    class Meta:
        model = solicitar
        fields = ('protocolo', 'senha')
        widgets = {
            'protocolo': forms.TextInput(attrs={
                'class': "form-input",
                'title': 'PROTOCOLO',
                'placeholder': "Número do requerimento"

        }),
            'senha': forms.TextInput(attrs={
                'class': "form-input",
                'title': 'SENHA',
                'placeholder': 'SENHA'
            }),
        }
        labels = {
            'senha': ('SENHA'),
            'protocolo': ('PROTOCOLO'),
        }

class recupraForm(forms.ModelForm):
    class Meta:
        model = recuperacao
        fields = ('nome', 'cpf', 'email', 'data', 'informacoes')
        widgets = {
            # 'clinica': forms.Select( attrs={
            # 'class': 'form-input-recupera',
            # 'aria-label': '.form-select-lg example'
            # }),
            'informacoes': forms.TextInput(attrs={
                'placeholder': 'Em que podemos te ajudar?',
                'class': 'form-input-recupera',
        }),
            'data': forms.DateInput(attrs={
                'placeholder': 'DATA EXAME:',
                'class': 'form-date-recupera',
                'type': 'date'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-input-recupera',
                'placeholder': 'E-MAIL:'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-input-recupera',
                'placeholder': 'CPF:'
            }),
            'nome': forms.TextInput(attrs={
                'class': 'form-input-recupera',
                # 'class': 'form-control',
                'placeholder': 'NOME DO PACIENTE:'
            })
        }
