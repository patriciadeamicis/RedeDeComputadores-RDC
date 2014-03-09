#coding:utf-8
import  unittest as u
from should_dsl import should, should_not

class Impressao(object):
	
	def __init__(self, nome_arquivo, usuario, impressora, copia=1):
		if(self._verifica_duplicidade_arquivos(nome_arquivo, usuario)):
			self.arquivo = nome_arquivo
			self.usuario = usuario
			self.impressora = impressora
			self.status = "aguardando"
			self.copia = copia
			Impressao.armazenar_impressao(self)
		else:
			raise TypeError("Atenção: Arquivos idênticos sendo enviados pelo mesmo usuário!")

	def get_usuario(self):
		return self.usuario

	def get_arquivo(self):
		return self.arquivo

	def get_copias(self):
		return self.copia

	def get_status(self):
		return self.status

	def set_status(self, novo_status):
		self.status = novo_status

if(__name__=='__main__'):
	u.main()
