import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dotenv import load_dotenv
import os




class UltaCrawlSpider(CrawlSpider):
    name = 'ulta_crawl'
    allowed_domains = ['www.ulta.com']
   

   
    

    def start_requests(self):
        yield scrapy.Request(url='https://www.ulta.com/hair-styling-products?N=26xf')

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='quick-view-prod']/a"), callback='parse_item', follow=True), 
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='next'])[2]")),
        
        
    )

  


    def parse_item(self, response):
        
        yield {
        
        'product_name': response.xpath("//span[@class='Text-ds Text-ds--title-5 Text-ds--left']/text()").get(),
        'brand-name': response.xpath("(//a[@class='Link_Huge Link_Huge--compact'])[1]/text()").get(),
        'rating': response.xpath("//div[@class='ReviewStars']/a/span/text()").get(),
        'ingredients': response.xpath("//details[@aria-controls='Ingredients']//div[@class='Markdown Markdown--body-2']/p/text()").getall(),
        'product_url': response.url,
        


        }

