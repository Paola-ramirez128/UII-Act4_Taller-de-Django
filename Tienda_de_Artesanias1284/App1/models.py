from django.db import models

# Create your models here.
class Provedores(models.Model):
    id_provedor = models.CharField(max_length=75, verbose_name="id_provedor")
    telefono = models.IntegerField(verbose_name="telefono")
    gmail = models.CharField(verbose_name="gmail", max_length=75)
    raiting = models.CharField(verbose_name="raiting", max_length=1)
    registro_fehca = models.DateField(verbose_name="registro fecha", max_length=75)
    tipo = models.CharField(verbose_name="tipo", max_length=10)
    provincia = models.CharField(verbose_name="provincia", max_length=75)

    class Meta:
        db_table = "Provedor"
        verbose_name = "Provedores"
        verbose_name_plural = "Provedor"

    def __str__(self):
        return self.id_provedor

class Sucursal(models.Model):
    id_sucursal = models.CharField(max_length=75, verbose_name="id_sucursal")
    direccion = models.CharField(verbose_name="direccion", max_length=75)
    ciudad = models.CharField(verbose_name="ciudad00", max_length=75)
    nombre = models.CharField(verbose_name="nombre", max_length=75)
    encargado = models.CharField(verbose_name="encargado", max_length=75)
    telefono = models.IntegerField(verbose_name="telefono")
    horario = models.IntegerField(verbose_name="horario")
    provedores_fk = models.ForeignKey(Provedores, on_delete=models.CASCADE)

    class Meta:
        db_table = "Sucursales"
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
