#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.root_layout_width = ""
        self.root_layout_heigh = ""
        self.root_layout_background_color = ""
        self.region_id = ""
        self.region_top = ""
        self.region_bottom = ""
        self.region_left = ""
        self.region_right = ""
        self.img_src = ""
        self.img_region = ""
        self.img_begin = ""
        self.img_dur = ""
        self.audio_src = ""
        self.audio_begin = ""
        self.audio_dur = ""
        self.textstream_src = ""
        self.textstream_region = ""
        self.etiquetas = []

    def starElement(self, etiqueta, atributo):
        if etiqueta == "root-layout":
            self.root_layout_width = atributo.get("width", "")
            self.root_layout_heigh = atributo.get("heigh", "")
            self.root_layout_background_color =
            atributo.get("background-color", "")
            self.root_layout = {"width": self.root_layout_width,
            "heigh": self.root_layout_heigh,
            "background-color": self.root_layout_background_color}
			self.etiquetas.append([etiqueta, self.root_layout])
        elif etiqueta == "region":
            self.region_id = atributo.get("id", "")
            self.region_top = atributo.get("top", "")
            self.region_bottom = atributo.get("bottom", "")
            self.region_left = atributo.get("left", "")
            self.region_right = atributo.get("right", "")
            self.region = {"id": self.region_id, "top": self.region_top,
            "bottom": self.region_bottom, "left": self.region_left,
            "right": self.region_right}
			self.etiquetas.append([etiqueta, self.region])
        elif etiqueta == "img":
            self.img_src = atributo.get("src", "")
            self.img_region = atributo.get("region", "")
            self.img_begin = atributo.get("begin", "")
            self.img_dur = atributo.get("dur", "")
            self.img = {"src":  self.img_src, "region": self.img_region,
            "begin": self.img_begi, "dur": self.img_dur}
			self.etiquetas.append([etiqueta, self.img])
        elif etiqueta == "audio":
            self.audio_src = atributo.get("src", "")
            self.audio_begin = atributo.get("begin", "")
            self.audio_dur = atributo.get("dur", "")
            sel.audio = {"src": self.audio_src, "begin": self.audio_begin,
            "dur": self.audio_dur}
			self.etiquetas.append([etiqueta, self.audio])
        elif etiqueta == "textstream":
            self.textstream_src = atributo.get("src", "")
            self.textstream_region = atributo.get("region", "")
            self.textstream = {"src": self.textstream_src,
            "region": self.textstream_region}
			self.etiquetas.append([etiqueta, self.textstream])

    #def get_tags(self):
        #print lista

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open("karaoke.smil"))
    #git clone url
    #git add fichero
    #git commit -m "comentario" fichero
    #git push
