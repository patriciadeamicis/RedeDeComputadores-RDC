import  unittest as u
from should_dsl import should, should_not

import time

class Impressora (object):
	def __init__(self, id_patrimonio, descricao, velocidade, servidor):
		self.id_patrimonio = id_patrimonio
		self.descricao = descricao
		self.velocidade = velocidade
		self.servidor = servidor
		self.impressoes = []

if(__name__=='__main__'):
	u.main()

