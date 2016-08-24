# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from itjuzi.items_investorinfo import ItjuziItem
import json
company_url = []
class InvestorinfoSpider(scrapy.Spider):
	name = "investorinfo"
	allowed_domains = ["itjuzi.com"]
	with open('/root/code/itjuzi/itjuzi/investorlinks.json') as data_file:
		data = json.load(data_file)
	for i in range(0,len(data)):
		for h in range(0,len(data[i]["website"])):
			company_url.append(data[i]["website"][h])
	start_urls = company_url
	
	headers = {
		"Accept": "*/*",
		"Accept-Encoding": "gzip,deflate",
		"Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
		"Connection": "keep-alive",
		"Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
		"Referer": "http://www.itjuzi.com/"
		}

	def parse(self, response):
		l = ItemLoader(item = ItjuziItem(),response=response)
		l.add_value('investor_link',response.url)
		l.add_value('investor_name',response.xpath("//span[@class='name marr10']/text()").extract()[0].encode('utf-8'))
		address = []
		a = filter(lambda x:x.strip(),response.xpath("//div[@class='boxed']/p[4]//text()").extract())
		for i in range(0,len(a)):
			address.append(filter(lambda x:x.strip(),a[i].split(' ')[-1]))
		l.add_value('address',address)
		investment_stage = []
		for i in range(0,len(response.xpath("//div[@class='list-tags yellow']//b//text()").extract())):
			investment_stage.append(response.xpath("//div[@class='list-tags yellow']//b//text()").extract()[i].encode('utf-8'))
		l.add_value('investment_stage',investment_stage)
		investment_field = []
		for i in range(0,len(response.xpath("//div[@class='list-tags darkblue']//b//text()").extract())):
			investment_field.append(response.xpath("//div[@class='list-tags darkblue']//b//text()").extract()[i].encode('utf-8'))
		l.add_value('investment_field',investment_field)
		e = filter(lambda x:x.strip(),response.xpath("//div[@class='pad block'][2]//text()").extract())
		investor_info = filter(lambda x:x.strip(),e[0].encode('utf-8'))
		l.add_value('investor_info',investor_info)
		investcase = []
		for i in range(1,len(response.xpath("//ul[@class='list-prodcase limited-itemnum']/li"))+1):
			a = response.xpath("//ul[@class='list-prodcase limited-itemnum']/li[%d]"%i).xpath(".//div[@class='right']//span//text()").extract()
			b = response.xpath("//ul[@class='list-prodcase limited-itemnum']/li[%d]//b/text()"%i).extract()
			c = response.xpath("//ul[@class='list-prodcase limited-itemnum']/li[%d]//@href"%i).extract()
			a.append(b[0].encode('utf-8'))
			a.append(c[0])
			investcase.append(a)
		l.add_value('investcase',investcase)
		work_experience = []
		work_company = []
		for h in range(1,len(response.xpath("//div[@class='sec'][3]").xpath(".//ul[@class='list-timeline-h']/li/span/span/a/text()").extract())+1):
			for i in range(1,len(response.xpath("//div[@class='sec'][3]").xpath(".//ul[@class='list-timeline-h']/li/span/a/@href").extract())+1):
				work_company.append(response.xpath("//div[@class='sec'][3]").xpath(".//ul[@class='list-timeline-h']/li[%d]/span/a/@href"%i).extract()[0])
				work_company.append(response.xpath("//div[@class='sec'][3]").xpath(".//ul[@class='list-timeline-h']/li[%d]/span/span/a/text()"%i).extract()[0].encode('utf-8'))
			work_experience.append(work_company[2*h-2:2*h])
		l.add_value('work_experience',work_experience)
		educational_experience = []
		edu_university = []
		for h in range(1,len(response.xpath("//div[@class='sec'][4]").xpath(".//ul[@class='list-timeline-h']/li/span/span/a/text()").extract())+1):
			for i in range(1,len(response.xpath("//div[@class='sec'][4]").xpath(".//ul[@class='list-timeline-h']/li/span/span[1]/a/@href").extract())+1):
				edu_university.append(response.xpath("//div[@class='sec'][4]").xpath(".//ul[@class='list-timeline-h']/li[%d]/span/span[1]/a/@href"%i).extract()[0])
				edu_university.append(response.xpath("//div[@class='sec'][4]").xpath(".//ul[@class='list-timeline-h']/li[%d]/span/span/a/text()"%i).extract()[0].encode('utf-8'))
			educational_experience.append(edu_university[2*h-2:2*h])
		l.add_value('educational_experience',educational_experience)
		service_organization = []
		service_organization.append(response.xpath("//div[@class='block-oneinc']").xpath(".//span[@class='picinfo']/span/text()").extract()[0].encode('utf-8'))
		service_organization.append(response.xpath("//div[@class='block-oneinc']//@href").extract()[0])
		l.add_value('service_organization',service_organization)
		print l
		return l.load_item()
