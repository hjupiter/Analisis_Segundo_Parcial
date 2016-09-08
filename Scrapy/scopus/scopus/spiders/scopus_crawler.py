# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scopus.items import ScopusItem


class ScopusCrawlerSpider(CrawlSpider):
    name = 'scopus_crawler'
    allowed_domains = ['scopus.com']
    start_urls = ['https://www.scopus.com/results/results.uri?cc=10&sort=plf-f&src=s&st1=ecuador&nlo=&nlr=&nls=&sid=3E07D6F35C9D50EEC0D052EC2FDBAC9F.53bsOu7mi7A1NSY7fPJf1g%3a10&sot=b&sdt=b&sl=37&s=AFFILCOUNTRY%28ecuador%29+AND+DOCTYPE%28cp%29&ss=plf-f&ps=r-f&editSaveSearch=&origin=resultslist&zone=resultslist']
    #start_urls = ['https://www.scopus.com/results/results.uri?sort=plf-f&src=s&st1=ecuador&nlo=&nlr=&nls=&sid=2261081F633B55F942523514F7824DFF.ZmAySxCHIBxxTXbnsoe5w%3a910&sot=b&sdt=b&sl=21&s=AFFILCOUNTRY%28ecuador%29&cl=t&offset=181&origin=resultslist&ss=plf-f&ws=r-f&ps=r-f&cs=r-f&cc=10&txGid=0']

    rules = (
        Rule(LinkExtractor(allow=r'record/'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(restrict_xpaths='//div[@id="footerResultsPerPage"]//div[nextPage]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        sel = scrapy.selector.Selector(response)
        questions = response.xpath('//div[@id = "profileleftside"]')
        for question in questions:
            item = ScopusItem()
            item['titulo'] = question.xpath("//div[@id='profileleftinside']/div/div[3]/h1/text()").extract()
            item['tipoDocumento'] = question.xpath("//div[@id='profileleftinside']/div/div[3]/h1/span/text()").extract()
            item['listaAutores'] = question.xpath("//div[@id='authorlist']/div/a/text()").extract()
            item['listaAfiliacion'] = question.xpath("//p[@id='affiliationlist']/span/text()").extract()
            item['abstract'] = question.xpath("//p[@id='recordAbs']/text()").extract()
            item['keywords'] = question.xpath("//div[@id='profileleftinside']/div/div[3]/p[@class='authKeywrdDes']/text()").extract()
            item['infoVolumen'] = question.xpath("//div[@id='profileleftinside']/div/div[1]/div[2]/text()").extract()
            item['publicadora'] = question.xpath("//div[@id='profileleftinside']/div/div[3]/div[13]/span/text()").extract()
            #print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
            #print question.xpath("//div[@id='profileleftinside']/div/div[3]/h1/text()").extract()
            #print question.xpath("//div[@id='profileleftinside']/div/div[3]/h1/span/text()").extract()
            #print question.xpath("//p[@id='affiliationlist']/span/text()").extract()
            #print question.xpath("//div[@id='profileleftinside']/div/div[3]/p[@class='authKeywrdDes']/text()").extract()
            #print question.xpath("//div[@id='profileleftinside']/div/div[1]/div[2]/text()").extract()
            #print question.xpath("//div[@id='profileleftinside']/div/div[3]/div[13]/span/text()").extract()
            #print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
            yield item