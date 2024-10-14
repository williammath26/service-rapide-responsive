from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from requests.auth import HTTPBasicAuth
from requests import get

from .models import clinica

from .forms import SolicitarForm, recupraForm

from .utils import enviar
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = SolicitarForm(request.POST)
        if form.is_valid():
            consulGet=form.save(commit=False)

            cli = clinica.objects.all()[0]

            retCaptura=capturaGet(url=cli.url, token=cli.token,
                       protocolo=consulGet.protocolo, senha=consulGet.senha)


            if retCaptura == {'data': []}:
                request.session['error'] = 'Protocolo ou senha não encontrado'
                return HttpResponseRedirect(reverse('home', args=[]))

            request.session['captura']=retCaptura
            consulGet.clinica=cli

            consulGet.save()

            consulGet.ip=str(ip_address(request))

            return HttpResponseRedirect(reverse('exame', args=[]))

    else:
        form = SolicitarForm()

    return render(request, 'home.html', {'form': form})

def recuperar(request):

    if request.method == 'POST':
        form = recupraForm(request.POST)
        if form.is_valid():
            cini=clinica.objects.all()[0]
            print(cini)
            dados=form.save(commit=False)
            dados.clinica=cini
            dadosForm={
                'nome': dados.nome,
                'cpf': dados.cpf,
                'email': dados.email,
                'data':dados.data,
                'clinica': cini,
                'informacoes': dados.informacoes,
            }
            enviar(dados=dadosForm)

            dados.save()
            request.session['sucess'] = 'Solicicitação enviada. Enviaremos um e-mail com as informções em breve'
            return HttpResponseRedirect(reverse('home', args=[]))

    else:
        form = recupraForm()

    return render(request, 'recuperar_senha.html', {'form': form})

def exames(request):

    solicitacao=(request.session['captura'])
    if solicitacao:
        request.session['captura']=''
        # solicitacao=''

        # return render(request, 'PaginaExames.html', {'solicitacao': solicitacao, 'paciente': ''})
        return render(request, 'PaginaExames.html', {'solicitacao': solicitacao, 'paciente': solicitacao['data']})
    else:
        return HttpResponseRedirect(reverse('home', args=[]))

def ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def capturaGet(url, token, protocolo, senha):
    try:
        send = get(
            url='{}/protocolo/externo/{}/{}'.format(url, protocolo,senha),
            # auth=HTTPBasicAuth(username=user, password=password),
            params='',  # {'nome':self.nome,'telefone':self.telefone}
            headers={'Authorization': f'Token {token}'},
        )
        return send.json()
    except Exception:
        return 0