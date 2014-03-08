#encoding:utf-8

import  unittest as u
from should_dsl import should, should_not
import time

class Conexao (object):
	def __init__(self, usuario):
		self.usuario=usuario
		self.data=(str(time.localtime()[2])+"/"+str(time.localtime()[1])+"/"+str(time.localtime()[0]));
		self.hora=(str(time.localtime()[3])+":"+str(time.localtime()[4])+":"+str(time.localtime()[5]))

if(__name__=='__main__'):
	u.main()

