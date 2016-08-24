# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from itjuzi.items import ItjuziItem
class PersonlinkSpider(scrapy.Spider):
    name = "personlink"
    allowed_domains = ["itjuzi.com"]
    start_urls = (
        'https://www.itjuzi.com/person?page=%d'%n for n in range(1,1714)
    )



    def parse(self, response):
	l = ItemLoader(item = ItjuziItem(),response=response)
	l.add_xpath('website',"////b[@class='title']//@href")
	return l.load_item()
