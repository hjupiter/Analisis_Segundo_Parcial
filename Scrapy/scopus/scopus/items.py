# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ScopusItem(Item):
    titulo = Field()
    tipoDocumento = Field()
    listaAutores = Field()
    listaAfiliacion = Field()
    abstract = Field()
    keywords = Field()
    infoVolumen = Field()
    publicadora = Field()