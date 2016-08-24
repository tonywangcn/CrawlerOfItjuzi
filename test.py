# -*- coding:utf-8 -*-
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
f = open('tag.html','r')
body = f.read()
span_text=Selector(text=body).xpath("/html/body/div[2]/div[2]/div[2]/div/div/div/div[1]/ul").extract()
for x in span_text:
	print x.encode('utf-8')
