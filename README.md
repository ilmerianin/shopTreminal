# shopTreminal

Задание:
-------

* Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
* Django Модель `Item` с полями `(name, description, price) `
* API с двумя методами:
    * GET `/buy/{id}`, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении
      этого метода c бэкенда с помощью python библиотеки stripe должен выполняться
      запрос` stripe.checkout.Session.create(...)` и полученный session.id выдаваться в результате запроса
    * GET `/item/{id}`, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о
      выбранном `Item` и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на `/buy/{id}`, получение
      session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout
      форму `stripe.redirectToCheckout(sessionId=session_id)`

* Залить решение на Github, описать запуск в README.md

* Просмотр Django Моделей в Django Admin панели - доступно по адресу `http://212.8.247.164/admin/`

* Запуск приложения на удаленном сервере, доступном для тестирования - запущенно на `http://212.8.247.164/shop/  (ssh личный (игнорируйте предупреждения о опастности))

Получение всех api ключей
-------------------------
при развертывании на локальной машине

Publishable key:
https://dashboard.stripe.com/apikeys

Secret key:
https://dashboard.stripe.com/apikeys

-------------------------

Запуск
-------

 
```
 git clone https://github.com/ilmerianin/shopTreminal.git  
 cd shopTreminal  
 conda env create  
 conda activate   
 python manage.py migrate  
 python manage.py runserver  

```

```

 git clone https://github.com/ilmerianin/shopTreminal.git   
 cd shopTreminal   
 python -m venv venv   
 .\venv\Scripts\activate   
 pip install -r requirements.txt   
 python manage.py migrate   
 python manage.py runserver   

```

Для админки:

```
python manage.py createsuperuser
```
 

