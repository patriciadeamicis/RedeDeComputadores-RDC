import  unittest as u
from should_dsl import should, should_not

class Usuario (object):
	def __init__(self, nome_usuario, senha):
		self.nome_usuario = nome_usuario
		self.senha = senha
		
if(__name__=='__main__'):
	u.main()
