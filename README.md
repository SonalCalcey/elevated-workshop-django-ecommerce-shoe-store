# Elevated Workshop - Django-Ecommerce-Shoe-Store

### Resources

*slides*: https://docs.google.com/presentation/d/1kygs28JsRayLuCaHpF3qXCrElGrtJWnvw9BvgrsoIns/edit?usp=sharing

#### Get up and running
```sh
cd .\ecommerce_shoe_store\src\
pip install -r requirements.txt
```
check *settings.py* file if database username/passowrd is correct and make *shoe_store* database in postgres
```sh
python manage.py migrate
```
databse now should have tables and some data populated!
```sh
python manage.py runserver
```
visit http://127.0.0.1:8000!
