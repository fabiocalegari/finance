from django.test import TestCase
from finance.apps import ImportSheet
from psycopg2.tests.testutils import unittest

# Create your tests here.
class TestImportSheet(unittest.TestCase):
    
    def testBasic(self):
        nome_pasta_de_trabalho = 'E:\\Google Drive\\Developer\\Python\\personal_finance\\Investimentos.xlsx'
        nome_planilha = 'Analitico'
        resultado = ImportSheet.import_movimentacao(None, nome_pasta_de_trabalho, nome_planilha)
        self.assertEquals(resultado, 'Fundo - XP Referenciado FI Referenciado DI')