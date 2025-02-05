from django.contrib import admin
from productos.models import Categoria
from productos.models import Producto
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render

class ProductoInline(admin.TabularInline):

    model = Producto
    extra = 0

class CategoriaAdmin(admin.ModelAdmin):
    inlines = [ProductoInline]


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    #fields =['categoria', 'fecha_publicacion', 'producto', 'imagen']

    fieldsets = [
        ("Relación", {"fields": ["categoria"]}),
        (
            "Datos generales",
            {
                "fields": [
                    'fecha_publicacion', 'producto', 'estado' , 'imagen' , 'descripcion'
                ]
            },
        ),
        
        (
            "Datos económicos",
            {
                "fields": [
                    'precio', 'stock', 'descuento' ,
                ]
            },
        ),

    ]
    list_display = ['producto', 'fecha_publicacion', 'tipo_de_producto', 'imagen', 'upper_case_name']
    ordering = ['-fecha_publicacion']
    list_filter = ('producto', 'fecha_publicacion',)
    search_fields=('producto', 'estado',)
    list_display_links = ('producto', 'fecha_publicacion',)
    actions=["publicar", "exportar_a_json", "ver_productos"]
    @admin.display(description='Name')
    def upper_case_name(self, obj):
        return ("%s %s" % (obj.producto, obj.estado)).upper()
    
    def publicar(self, request, queryset):
        registro = queryset.update(estado="Publicado")
        
        if registro == 1:
            mensaje = "1 registro actualizado"
        else:
            mensaje = "%s registros actualizados" % registro
        self.message_user(request, "%s exitosamente" % mensaje)    
    
    publicar.short_description = "Pasar a publicado"

    def exportar_a_json(self, request, queryset):
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response)
        return response
    
    def ver_productos(self, request, queryset):
        params={}
        productos=Producto.objects.all
        params["productos"]=productos
        return render(request, "admin/productos/productos.html", params)
    
    ver_productos.short_description = "Ver productos"
    
    
#admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)


#admin.site.register(Categoria)
#admin.site.register(Producto)