# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from itjuzi.items_personinfo import ItjuziItem
import json


class PersoninfoSpider(scrapy.Spider):
	name = "personinfo"
	company_url = []
	allowed_domains = ["itjuzi.com"]
	with open('/root/code/itjuzi/itjuzi/personlink.json') as data_file:
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
		l.add_value('person_link',response.url)
		l.add_value('person_name',response.xpath("//span[@class='name marr10']/text()").extract()[0].encode('utf-8'))
		address = []
		a = filter(lambda x:x.strip(),response.xpath("//div[@class='boxed']/p[4]//text()").extract())
		for i in range(0,len(a)):
			address.append(filter(lambda x:x.strip(),a[i].split(' ')[-1]).encode('utf-8'))
		l.add_value('address',address)
		l.add_value('person_info',filter(lambda x:x.strip(),response.xpath("//div[@class='block block-v']/text()").extract()[0]).encode('utf-8'))
		enterprise_experience = []
		for i in range(0,len(response.xpath("//ul[@class='list-timeline haslogin']/li/a/@href").extract())):
			for h in range(0,2):
				company = []
				link  = response.xpath("//ul[@class='list-timeline haslogin']/li/a/@href").extract()[i]
				com_name = response.xpath("//span[@class='long']/text()").extract()[i].encode('utf-8')
				company.append(link)
				company.append(com_name)
			enterprise_experience.append(company)
		l.add_value('enterprise_experience',enterprise_experience)
		work_experience = []
		for h in range(1,len(response.xpath("//div[@class='sec'][3]").xpath(".//ul[@class='list-timeline-h']/li/span/span/a/text()").extract())+1):
			for i in range(1,len(response.xpath("//div[@class='sec'][3]").xpath(".//ul[@class='list-timeline-h']/li/span/a/@href").extract())+1):
				work_company = []
				work_company.append(response.xpath("//div[@class='sec'][3]").xpath(".//ul[@class='list-timeline-h']/li[%d]/span/a/@href"%i).extract()[0])
				work_company.append(response.xpath("//div[@class='sec'][3]").xpath(".//ul[@class='list-timeline-h']/li[%d]/span/span/a/text()"%i).extract()[0].encode('utf-8'))
			work_experience.append(work_company[2*h-2:2*h])
		l.add_value('work_experience',work_experience)
		educational_experience = []
		for h in range(1,len(response.xpath("//div[@class='sec'][4]").xpath(".//ul[@class='list-timeline-h']/li/span/span/a/text()").extract())+1):
			for i in range(1,len(response.xpath("//div[@class='sec'][4]").xpath(".//ul[@class='list-timeline-h']/li/span/span[1]/a/@href").extract())+1):
				edu_university = []
				edu_university.append(response.xpath("//div[@class='sec'][4]").xpath(".//ul[@class='list-timeline-h']/li[%d]/span/span[1]/a/@href"%i).extract()[0])
				edu_university.append(response.xpath("//div[@class='sec'][4]").xpath(".//ul[@class='list-timeline-h']/li[%d]/span/span/a/text()"%i).extract()[0].encode('utf-8'))
			educational_experience.append(edu_university[2*h-2:2*h])
		l.add_value('educational_experience',educational_experience)
		print l
		return l.load_item()
