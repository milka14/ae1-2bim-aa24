from django.contrib import admin

# Importar las clases del modelo
from campeonato.models import equipo_futbol

# Agregar la clase Equipo para administrar desde
# interfaz de administración
admin.site.register(equipo_futbol)
