from django.contrib import admin

# Register your models here.
from finance.models import TipoInvestimento, Investimento, TipoMovimento

class CrudTipoInvestimento(admin.ModelAdmin):
    class Meta:
        model = TipoInvestimento
        
class CrudInvestimento(admin.ModelAdmin):
    class Meta:
        model = Investimento
        
class CrudTipoMovimento(admin.ModelAdmin):
    class Meta:
        model = TipoMovimento
                
admin.site.register(TipoInvestimento, CrudTipoInvestimento)
admin.site.register(Investimento, CrudInvestimento)
admin.site.register(TipoMovimento, CrudTipoMovimento)