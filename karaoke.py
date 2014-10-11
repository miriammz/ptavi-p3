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

	def __str__(self):  #imprime la lista
		print "2"

	def do_local(self):	 #descarga recursos remotos
		print "6"

if __name__ == "__main__":
	try:	
		smil = sys.argv[1]
		karaoke = KaraokeLocal(smil)
		karaoke.__str__()
		karaoke.do_local()
	except:
		print "Usage: python karaoke.py file.smil"
		sys.exit() 
