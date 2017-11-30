# -*- coding:utf-8 -*-
import scrapy

class ShiyanlouSpider(scrapy.Spider):
    name = 'shiyanlou-courses'
    def start_requests(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        urls = (url_tmpl.format(i) for i in range(1,23))
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        for course in response.css('li.col-12'):
            yield{
                    'name':course.css('div.mb-1 h3 a::text').extract(),
                    'update_time':course.css('div.mt-2 relative-time::attr(datetime)').extract_first()
                }
