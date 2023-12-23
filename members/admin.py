from django.contrib import admin
from .models import kategori, produk

# Register your models here.
class produkAdmin( admin.ModelAdmin):
     list_display = ("namaproduk", "harga")

admin.site.register(kategori)
admin.site.register(produk , produkAdmin)
