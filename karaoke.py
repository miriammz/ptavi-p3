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

    def __str__(self):  # imprime la lista
        for sublista in self.lista:
            etiqueta = sublista[0]
            sublista_atrib = sublista[1]
            print etiqueta + "\t",
            for atributo in sublista_atrib:
                if sublista_atrib[atributo] != "":
                    print atributo + "=", sublista_atrib[atributo], "\t",
            print

    def do_local(self):     # descarga recursos remotos
        for sublista in self.lista:
            etiqueta = sublista[0]
            sublista_atrib = sublista[1]
            for atributo in sublista_atrib:
                if sublista_atrib[atributo] != "" and atributo == "src":
                    recurso = sublista_atrib[atributo]
                    os.system("wget -q " + recurso)
                    lista = recurso.split("/")
                    lista = lista[-1]
                    sublista_atrib[atributo] = lista
                    print sublista_atrib[atributo]

if __name__ == "__main__":
    try:
        smil = sys.argv[1]
        karaoke = KaraokeLocal(smil)
        karaoke.__str__()
        karaoke.do_local()
    except:
        print "Usage: python karaoke.py file.smil"
        sys.exit()
# si quiero imprimir sin espacios entre el "=", me da usage error
