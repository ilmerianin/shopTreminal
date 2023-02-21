from django.shortcuts import render
from django.shortcuts import redirect
from django.conf.urls.static import static

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import stripe
from dotenv import load_dotenv, find_dotenv
from django.views import generic
from .models import item
from django.conf import settings


class itemListView(generic.ListView):
    ''' Шаблон длдя получения списка  
    /application_name/.html - путь
    '''
    model = item

class itemDetalView(generic.detail.DetailView):
    model = item

def indexItem(request):
    ''' Заголовок для платёжного терминалла '''
    
    num_items = item.objects.all().count()
    return render(
        request,
        'index.html',
        context = {'num_items': num_items}
        )

def configS(request):
    ''' запрос config отдаёт api key для post? запроса'''
    
    data = get_config()
    
    dataJ= JsonResponse(data)

    return HttpResponse(dataJ)

def subMit(request):
    ''' вывод окна удачной продажи '''
    return render(request,
            'submitted.html',
            #context = { }
            )

def checkout(reuest):
    ''' продажа и выдача ссылки  '''
    id_item = reuest.META['QUERY_STRING']
    itemId =  item.objects.get(pk=id_item)
    Sess_url =create_checkout_session(itemId)

    return  HttpResponseRedirect(Sess_url) #redirect(Sess_url)

def checkoutSess(reuest):
    ''' продажа и выдача essions для вызова из js '''
    id_item = reuest.META['QUERY_STRING']
    itemId =  item.objects.get(pk=id_item)
    
    Sess =create_session(itemId)
    return  Sess #redirect(Sess_url)


def get_config():
    stripe.api_key = settings.STRIP_PUBLIC_KEY
   
    return {'publishableKey': stripe.api_key}


def create_verification_session():
    '''
    сессия регпстрации пользователя 
    возвращает client_cecret Он одноразовый и истекает через 24 часа. Не сохраняйте его, не регистрируйте,
    
    '''
    stripe.api_key = settings.STRIP_SECRET_KEY
    try:
        verification_session = stripe.identity.VerificationSession.create(
            type='document',
            metadata={
                'user_id': '{{USER_ID}}',
            }
        )
              
        return JsonResponse({'client_secret': verification_session.client_secret})
    except stripe.error.StripeError as e:
        
        return JsonResponse({'error': {'message': str(e)}}), 400
    except Exception as e:
        
        return JsonResponse({'error': {'message': str(e)}}), 400
    
    
def create_checkout_session(itemI):
  '''  процесс оплпты '''

  stripe.api_key = settings.STRIP_SECRET_KEY
  session = stripe.checkout.Session.create(
    line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': itemI.name,
          "description": itemI.description,
          #"default_price": itemI.price,
        },
        #'unit_amount'
        "unit_amount_decimal":  itemI.price * 100,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url=settings.OUR_DOMAIN +'/shop/successCheck',
    cancel_url=settings.OUR_DOMAIN + '/shop/cancel',
  )
   
  return session.url

def create_session(itemI):
    '''  Получение  сессии '''
    
    stripe.api_key = settings.STRIP_SECRET_KEY
    try:
        checkout_session = stripe.checkout.Session.create(
         #payment_mathod_types=['card'], # возможно не очень нужен
         #success_url="https://example.com/success",
         line_items=[{
          'price_data': {
            'currency': 'usd',
            'product_data': {
              'name': itemI.name,
              "description": itemI.description,
              #"default_price": itemI.price,
            },
            #'unit_amount'
            "unit_amount_decimal":  itemI.price * 100,
          },
          'quantity': 1,
        }],
        mode='payment',
        success_url=settings.OUR_DOMAIN +'/shop/successCheck',
        cancel_url=settings.OUR_DOMAIN + '/shop/cancel',
        )
        
        # client_secret = verification_session.client_secret #
        
        return JsonResponse({'id': checkout_session.id})
    except stripe.error.StripeError as e:
        
        return JsonResponse({'error': {'message': str(e)}}), 400
    except Exception as e:
        
        return JsonResponse({'error': {'message': str(e)}}), 400


   



