from django.apps import AppConfig
from openpyxl import load_workbook
from _datetime import date
from finance.models import Investimento, TipoMovimento, Movimento


class FinanceConfig(AppConfig):
    name = 'finance'

#support classes
class ImportSheet():
    def import_movimentacao(self, nome_pasta_de_trabalho, nome_planilha):
        workbook = load_workbook(nome_pasta_de_trabalho, data_only=True)
        sheet_ranges = workbook[nome_planilha]

        linha = 2
        sheet_dsc_investimento = ''
        sheet_data_movimento = date.today()
        sheet_valor_movimento = 0.0
        
        while sheet_dsc_investimento is not None:
            dsc_investimento = sheet_ranges['A'+linha.__str__()].value
            dsc_tipo_movimento = sheet_ranges['D'+linha.__str__()].value
            sheet_data_movimento = date.strftime(sheet_ranges['B'+linha.__str__()].value, '%Y-%m-%d')
            sheet_valor_movimento = sheet_ranges['E'+linha.__str__()].value
            
            sheet_investimento = Investimento.objects.filter(descricao=dsc_investimento).get()
            sheet_tipo_movimento = TipoMovimento.objects.filter(descricao=dsc_tipo_movimento).get()
            
            movimento = Movimento(investimento = sheet_investimento, tipo_movimento = sheet_tipo_movimento, data_movimento = sheet_data_movimento, valor_movimento = sheet_valor_movimento)
            movimento.save()
            
            print(movimento)
            
            linha = linha + 1

        return linha