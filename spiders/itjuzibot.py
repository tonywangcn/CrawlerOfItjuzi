#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from itjuzi.items import ItjuziItem
import json


class ItjuziSpider(scrapy.Spider):
    company_url = []
    name = "itjuzi"
    allowed_domains = ["itjuzi.com"]
    with open('/root/code/itjuzi/itjuzi/links.json') as data_file:
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
        l.add_value('company_link',response.url)
        l.add_value('company_name',response.xpath("//ul[@class='bread dark']/li[3]/a/text()").extract()[0].encode('utf-8'))
        l.add_value('scope',response.xpath("//span[@class='scope c-gray-aset']/a[1]/text()").extract()[0].encode('utf-8'))
        l.add_value('subscope',response.xpath("//span[@class='scope c-gray-aset']/a[2]/text()").extract()[0].encode('utf-8'))
        prov = []
        for i in range(1,len(response.xpath("//span[@class='loca c-gray-aset']/a/text()").extract())+1):
            prov.append(response.xpath("//span[@class='loca c-gray-aset']/a[%d]/text()"%i).extract()[0].encode('utf-8'))
        l.add_value('prov',prov)
        l.add_value('website',response.xpath("//div[@class='link-line']/a[3]/text()").extract()[1].strip())
        tag = []
        for i in range(0,len(response.xpath("//span[@class='tag']/text()").extract())):
            tag.append(response.xpath("//span[@class='tag']/text()").extract()[i].encode('utf-8'))
        l.add_value('tag',tag)
        l.add_value('description',response.xpath("//div[@class='des']/text()").extract()[0].strip().encode('utf-8'))
        l.add_value('full_name',response.xpath("//div[@class='des-more']//span/text()").extract()[0].encode('utf-8'))
        l.add_value('regtime',response.xpath("//div[@class='des-more']//span/text()").extract()[1][5:])
        invest_date = []
        for i in range(0,len(response.xpath("//table[@class='list-round-v2']").xpath("//span[@class='date c-gray']/text()").extract())):
            invest_date.append(response.xpath("//table[@class='list-round-v2']").xpath("//span[@class='date c-gray']/text()").extract()[i])
        l.add_value('invest_date',invest_date)
        invest_round = []
        for i in range(0,len(response.xpath("//table[@class='list-round-v2']").xpath("//span[@class='round round-afterdate']//text()").extract())):
            invest_round.append(response.xpath("//table[@class='list-round-v2']").xpath("//span[@class='round round-afterdate']//text()").extract()[i])

        l.add_value('invest_round',invest_round)
        financing_amount = []
        for i in range(0,len(response.xpath("//table[@class='list-round-v2']").xpath("//span[@class='finades']//text()").extract())):
            financing_amount.append(response.xpath("//table[@class='list-round-v2']").xpath("//span[@class='finades']//text()").extract()[i])
        l.add_value('financing_amount',financing_amount)
        investFirm = []
        for i in range(1,len(response.xpath("//table[@class='list-round-v2']//tr").extract())+1):
            investFirm.append(filter(lambda x:x.strip(),response.xpath("//table[@class='list-round-v2']//tr[%d]/td[4]//text()"%i).extract())[0].encode('utf-8'))
        l.add_value('investfirm',investFirm)
        team = []
        for h in range(1,len(response.xpath("//ul[@class='list-prodcase limited-itemnum']//li").extract())+1):
            team_a = []
            for i in range(0,len(filter(lambda x:x.strip(),response.xpath("//ul[@class='list-prodcase limited-itemnum']//li[%d]"%h).xpath(".//div[@class='right']//text()").extract()))):
                a = filter(lambda x:x.strip(),filter(lambda x:x.strip(),response.xpath("//ul[@class='list-prodcase limited-itemnum']//li[%d]"%h).xpath(".//div[@class='right']//text()").extract())[i])
                team_a.append(a)
                team_a.append(response.xpath("//h4[@class='person-name']").xpath(".//a[@class='title']/@href").extract()[h-1])
            team.append(team_a)


        l.add_value('team',team)
        l.add_value('phone',response.xpath("//ul[@class='list-block aboutus']/li[1]//span//text()").extract()[0].encode('utf-8'))
        l.add_value('email',response.xpath("//ul[@class='list-block aboutus']/li[2]//span//text()").extract()[0].encode('utf-8'))
        l.add_value('address',response.xpath("//ul[@class='list-block aboutus']/li[3]//span//text()").extract()[0].encode('utf-8'))
        l.add_xpath('follower',"//div[@class='block-numberpad colum3']/div[1]//b//text()")
        l.add_xpath('comment',"//div[@class='block-numberpad colum3']/div[2]//b//text()")
        l.add_value('pageview',response.xpath("//div[@class='block-numberpad colum3']/div[3]//b//text()").extract()[0].strip())
        print l
        return l.load_item()
#			for x,y,z in zip(item["title"],item["link"],item["desc"]):
#				print x.encode("utf-8") = item["title"],y.encode("utf-8"),z.encode("utf-8") 
