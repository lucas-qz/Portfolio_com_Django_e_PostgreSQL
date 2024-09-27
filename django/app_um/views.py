from django.shortcuts import render,redirect
from datetime import datetime
from . import models
import pytz
import requests
from user_agents import parse
import requests

def portfolio(request):
# id da sessão ---------------------------------------------------------------   
    request.session['ds'] = request.session.get('ds', 0)
    session_id = request.session.session_key
    if session_id is None:
        return redirect('portfolio2')
    else:
        session_id = request.session.session_key
# ip, pais, estado, cidade ---------------------------------------------------
        response = requests.get('http://ipinfo.io')
        dict = response.json()
        ip1  = request.META['REMOTE_ADDR']
        #ip2 = dict['ip']
        pais = dict['country']
        estado = dict['region']
        cidade = dict['city']   
# referer -----------------------------------------------------------------------
# url ---------------------------------------------------------------------------
        referer = request.META.get('HTTP_REFERER', None)
        if referer is not None:
            url ='/'
        else:
            url = request.get_full_path() # pega tudo que vem após o dominio
# device ------------------------------------------------------------------------
        user_agent = request.META['HTTP_USER_AGENT']
        ua = parse(user_agent)
        device = str(ua)
# data ----------------------------------------------------------------------------
        from django.utils import timezone
        from datetime import timedelta
        date_added = timezone.now() - timedelta(hours=3)
# abaixo o insert no banco
        models.Rastreio.objects.create(session_id=session_id, ip=ip1, pais=pais, estado=estado, cidade=cidade, referer=referer, url=url, device=device, date_added=date_added)   
        return render(request, 'index.html')

def portfolio2(request):
    return redirect('portfolio')

def r(request,id):
    session_id = request.session.session_key
    if id=='linkedin':  
        link = 'https://www.linkedin.com/in/seu_linkedin/'
    elif id=='github':   
        link = 'https://github.com/seu_github'
    elif id=='whatsapp':   
        link = 'https://wa.me/5511977777777'
    elif id=='email':  
        link = 'email'  
    elif id=='curriculo':
        link = '../static/src/pdf/cv.pdf'      

    elif id=='projeto1_github':
        link = 'https://github.com/seu_github'   
    elif id=='projeto1_ver':
        link = 'http://lucasqz.com.br:5000'   
		
    elif id=='projeto2_github':
        link = 'https://github.com/seu_github'     
    elif id=='projeto2_ver':
        link = 'http://lucasqz.com.br'     
		
    elif id=='projeto3_github':
        link = '#'     
    elif id=='projeto3_ver':
        link = '#'   
		
    elif id=='projeto4_github':
        link = '#'     
    elif id=='projeto4_ver':
        link = '#'     
		
    elif id=='projeto5_github':
        link = '#'     
    elif id=='projeto5_ver':
        link = '#'   
		
    elif id=='projeto6_github':
        link = '#'     
    elif id=='projeto6_ver':
        link = '#' 

    requests.get(f'http://{request.META['HTTP_HOST'] }') 
    ultimo = models.Rastreio.objects.filter().last() 
    models.Rastreio.objects.filter(id=ultimo.id).update(session_id=session_id, url=id)      
    return redirect(f'{link}')  

def email(request): 
    return render(request,"email.html")   


 
