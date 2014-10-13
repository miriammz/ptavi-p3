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
        parser.parse(open(sys.argv[1]))
        self.lista = cHandler.get_tags()

    def __str__(self):  # imprime la lista
        valor = ""
        for sublista in self.lista:
            etiqueta = sublista[0]
            dic = sublista[1]
            valor += "\n" + etiqueta + "\t"
            for atributo in dic:
                if dic[atributo] != "":
                    valor += atributo + "=" + '"' + dic[atributo] + '"' + "\t"
        return valor

    def do_local(self):     # descarga recursos remotos
        for sublista in self.lista:
            etiqueta = sublista[0]
            dic = sublista[1]
            for atributo in dic:
                if dic[atributo] != "" and atributo == "src":
                    recurso = dic[atributo]
                    os.system("wget -q " + recurso)
                    lista = recurso.split("/")
                    lista = lista[-1]
                    dic[atributo] = lista

if __name__ == "__main__":
    try:
        karaoke = KaraokeLocal(sys.argv[1])
    except KeyError:
        print "Usage: python karaoke.py file.smil"
        sys.exit()
    print karaoke.__str__()
    karaoke.do_local()
    print karaoke.__str__()
