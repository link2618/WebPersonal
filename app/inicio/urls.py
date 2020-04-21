from django.urls import path, include

from app.inicio.views import (
    Inicio,
    )

app_name = "inicio_app"

#La url para que funcione debe llamarse desde el archivo principal de url
urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
]
