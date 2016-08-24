# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from itjuzi.items_investfirminfo import ItjuziItem
import json


class InvestfirminfoSpider(scrapy.Spider):
	name = "investfirminfo"
	company_url = []
	allowed_domains = ["itjuzi.com"]
	with open('/root/code/itjuzi/itjuzi/investfirm.json') as data_file:
		data = json.load(data_file)
	for i in range(0,len(data)):
		for h in range(0,len(data[i]["link"])):
			company_url.append(data[i]["link"][h])
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
		l.add_value('firm_link',response.url)
		l.add_value('firm_site',response.xpath("//div[@class='boxed rel']").xpath(".//span[@class='links']//@href").extract())
		l.add_value('firm_info',filter(lambda x:x.strip(),response.xpath("//div[@class='block block-inc-info']/div/text()").extract()[0])[0].encode('utf-8'))
		investment_field = []
		for i in range(0,len(response.xpath("//div[@class='list-tags darkblue']//b//text()").extract())):
			investment_field.append(response.xpath("//div[@class='list-tags darkblue']//b//text()").extract()[i].encode('utf-8'))
		investment_round = []
		l.add_value('investment_field',investment_field)
		for i in range(0,len(response.xpath("//div[@class='list-tags yellow']//b/text()").extract())):
			investment_round.append(response.xpath("//div[@class='list-tags yellow']//b/text()").extract()[i].encode('utf-8'))
		l.add_value('investment_round',investment_round)
		investment_cube = []
		for i in range(0,len(response.xpath("//td[@class='date']/span/text()").extract())):
			for h in range(6):
				investment_event = []
				date = response.xpath("//td[@class='date']/span/text()").extract()[i]
				company_name = response.xpath("//td[@class='title']//b/text()").extract()[i].encode('utf-8')
				company_scope = response.xpath("//td[@class=' mobile-none']/span/text()").extract()[i].encode('utf-8')
				invest_round = response.xpath("//table[@class='list-invecase limited-itemnum haslogin needfilter']").xpath(".//td[5]/span/text()").extract()[i].encode('utf-8')
				amount = response.xpath("//table[@class='list-invecase limited-itemnum haslogin needfilter']").xpath(".//td[6]/span/text()").extract()[i].encode('utf-8')
				investment_event.append(date)
				investment_event.append(company_name)
				investment_event.append(company_scope)
				investment_event.append(invest_round)
				investment_event.append(amount)
			investment_cube.append(investment_event)
		l.add_value('investment_cube',investment_cube)
		incumbent_emp = []
		for i in range(0,len(response.xpath("//div[@class='sec'][3]").xpath(".//ul[@class='list-prodcase limited-itemnum width100']/li/a/@href").extract())):
			for h in range(0,2):
				investor = []
				investor_link = response.xpath("//div[@class='sec'][3]").xpath(".//ul[@class='list-prodcase limited-itemnum width100']/li/a/@href").extract()[i]
				investor_name = response.xpath("//div[@class='sec'][3]").xpath(".//ul[@class='list-prodcase limited-itemnum width100']").xpath(".//h4[@class='person-name']/b/text()").extract()[i].encode('utf-8')
				investor.append(investor_link)
				investor.append(investor_name)
			incumbent_emp.append(investor)
		l.add_value('incumbent_emp',incumbent_emp)
		ex_emp = []
		for i in range(0,len(response.xpath("//div[@class='sec'][4]").xpath(".//ul[@class='list-prodcase limited-itemnum width100']/li/a/@href").extract())):
			for h in range(0,2):
				ex_investor = []
				ex_investor_link = response.xpath("//div[@class='sec'][4]").xpath(".//ul[@class='list-prodcase limited-itemnum width100']/li/a/@href").extract()[i]
				ex_investor_name = response.xpath("//div[@class='sec'][4]").xpath(".//ul[@class='list-prodcase limited-itemnum width100']").xpath(".//h4[@class='person-name']/b/text()").extract()[i].encode('utf-8')
				ex_investor.append(investor_link)
				ex_investor.append(investor_name)
			ex_emp.append(investor)
		l.add_value('ex_emp',ex_emp)
		print l
		return l.load_item()
