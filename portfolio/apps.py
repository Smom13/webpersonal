from django.apps import AppConfig


class PortfolioConfig(AppConfig):  #Se copio el nombre de la funcion  y se llama en los settings del proyecto en el apartado apps
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
    verbose_name = 'Portafolio'
