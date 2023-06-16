from class_conjunt_individus import *
from collections import namedtuple
from bintree import *



class Pocoyo:
	def __init__(self):
		self._arbre=self.llegeix_bintree_int(self) 
		
	def llegeix_bintree_int(self,marca=0):
	
		x = [3, 1, 4, 0, 0, 2, 0, 0, 5, 0,0]
		for i in x:
			if i != marca:
				l = self.llegeix_bintree_int(marca)
				r = self.llegeix_bintree_int(marca)
				
				return BinTree(x,l,r)
			else:
				return BinTree()	
			
	def distribucio_trets(self, tret):
		arb_aux=BinTree(self.get_root(), self.get_left(), self.get_right())
		if arb_aux.get_left().te_tret(tret)==0 and arb_aux.get_left().leaf():
			poda_subarbre(arb_aux.get_left)
		if arb_aux.get_right().te_tret(tret)==0 and arb_aux.get_right().leaf:
			poda_subarbre(arb_aux.right)
		distribucio_trets(arb_aux.get_left)
		distribucio_trets(arb_aux.get_right)
		result = arb_aux.distribucio_inorder(tret)
		return result 


pocoyo=Pocoyo()
pocoyo.get_root()
pocoyo.afegir_tret(qwert1, 1)
print(pocoyo.distribucio_trets(qwert1))
