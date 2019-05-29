# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonMobileDetailsItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/s?k=Mobiles&ref=nb_sb_noss_2']

    page_number = 2

    def parse(self, response):
        items = AmazonMobileDetailsItem()

        mobile_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        mobile_review = response.css('.a-size-small .a-size-base').css('::text').extract()
        mobile_price = response.css('.a-price:nth-child(1) .a-price-whole').css('::text').extract()
        mobile_imagelink = response.css('.s-image::attr(src)').extract()


        items['mobile_name'] = mobile_name
        items['mobile_review'] = mobile_review
        items['mobile_price'] = mobile_price
        items['mobile_imagelink'] = mobile_imagelink

        yield items

        next_page = 'https://www.amazon.in/s?k=Mobiles&page=' + str(AmazonSpiderSpider.page_number) + '&qid=1559110705&ref=sr_pg_2'


        if AmazonSpiderSpider.page_number<=5:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)