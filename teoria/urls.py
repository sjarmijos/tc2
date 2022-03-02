from django.urls import path
from .views import conjunto, operacion, algebra

urlpatterns=[
    path('conjuntos/', conjunto, name='Tconjuntos'),
    path('operaciones/', operacion, name='Toperaciones'),
    path('algebra/', algebra, name='Talgebra'),
]