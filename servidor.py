# -*- coding: cp1252 -*-
import  unittest as u
from should_dsl import should, should_not
from computador import Computador

class Servidor (Computador):
	def __init__(self, id_patrimonio, desc, max_HD, max_memoria, max_buffer, max_bufferImpressao):
		Computador.__init__(self, id_patrimonio, desc, max_HD, max_memoria)
		self.tam_buffer = max_buffer;
		self.tam_buffer_impressao = max_bufferImpressao
		self.impressoras = []

if(__name__=='__main__'):
	u.main()

