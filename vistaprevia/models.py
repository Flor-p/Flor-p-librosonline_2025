from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return '%s' % self.nombre


class Producto(models.Model):
    producto = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField('Fecha de publicación')
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", blank=True, null=True)
    categoria = models.ManyToManyField(Categoria)
    
def __str__(self, ):
    return self.producto + "---" + str(self.fecha_publicacion)
         

