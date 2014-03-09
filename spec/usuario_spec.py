#coding:utf-8
import unittest
from should_dsl import should, should_not
from usuario import Usuario
from estacao import Estacao
from servidor import Servidor
from impressora import Impressora
from impressao import Impressao

class usuarioSpec (unittest.TestCase):
	def setUp(self):
		self.estacao = Estacao(1,"estacao 1 do microdromo", 250, 1, "fila 1")
		self.servidor = Servidor(1,"servidor de impressao do microdromo", 500, 2, 50, 100)
		self.impressora1 = Impressora(1, "Impressora do microdromo", 350, self.servidor)
		self.impressora2 = Impressora(2, "Impressora do microdromo", 400, self.servidor)
		self.usuario1 = Usuario("edson","eds")
		self.usuario2 = Usuario("patty","pat")

	def it_test_enviarArqImprimir(self):
		self.estacao.iniciar_conexao(self.usuario)
		self.usuario.enviar_arq_imprimir("apostila.pdf", self.impressora1)
		Impressao.obtem_impressoes() |should| have(1).itens
		self.usuario.enviar_arq_imprimir("apostila.pdf", self.impressora2) |should| throw (TypeError, message = "Atenção: Foi identificado na rede arquivos idênticos sendo enviados pelo mesmo usuário")

if(__name__=='__main__'):
	unittest.main()

