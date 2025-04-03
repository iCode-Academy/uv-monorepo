# Аппликейшнууд

Энэ хавтас нь Django аппликейшнуудыг агуулна. Энд таны төслийн бүх Django аппликейшнууд байрлана.

## Аппликейшн бүтэц

Аппликейшн бүр дараах бүтэцтэй байна:

```
app_name/
├── __init__.py
├── admin.py
├── apps.py
├── migrations/
├── models.py
├── tests.py
├── urls.py
└── views.py
```

## Шинэ аппликейшн үүсгэх

Шинэ аппликейшн үүсгэхдээ дараах командыг ашиглана:

```bash
python manage.py startapp app_name src/apps/app_name
```

Дараа нь `INSTALLED_APPS` жагсаалтад нэмнэ:

```python
INSTALLED_APPS = [
    # ...
    'src.apps.app_name',
    # ...
]
```
