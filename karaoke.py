#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler 
import sys
import os


class KaraokeLocal(smallsmilhandler.SmallSMILHandler):

	def __init__(self, fichero):
		parser = make_parser()
		cHandler = smallsmilhandler.SmallSMILHandler()
		parser.setContentHandler(cHandler)
		parser.parse(open(smil))	
		self.lista = cHandler.get_tags()		

if __name__ == "__main__":
	try:	
		smil = sys.argv[1]
		karaoke = KaraokeLocal(smil)
		 #print "hola"
	except:
		print "Usage: python karaoke.py file.smil"
		sys.exit() 
	


		
		


