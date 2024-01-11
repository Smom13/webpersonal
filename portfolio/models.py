from django.db import models

class Project(models.Model): # creación de tabla
    title = models.CharField(max_length=200, verbose_name = "Título") #campo de caracteres 
    description = models.TextField(verbose_name = "Descripción") #texto mas amplio
    image = models.ImageField(verbose_name = "Imagen", upload_to='projects')
    link = models.URLField(null=True,blank=True,verbose_name="Url del proyecto")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creación") #fecha y hora auto
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de edición") # se actualiza cuando modifiquemos
    
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title