from django.contrib import admin
from .models import VPS


@admin.register(VPS)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('uid', 'cpu', 'ram', 'hdd', 'status')
