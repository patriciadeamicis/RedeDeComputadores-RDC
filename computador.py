import  unittest as u
from should_dsl import should, should_not
import time

class Computador (object):
        lista_computadores=[]

	def __init__(self, id_patrimonio, desc, max_HD, max_memoria):
		self.id_patrimonio = id_patrimonio
		self.descricao = desc
		self.tam_HD = max_HD
		self.tam_memoria = max_memoria

if(__name__=='__main__'):
	u.main()
