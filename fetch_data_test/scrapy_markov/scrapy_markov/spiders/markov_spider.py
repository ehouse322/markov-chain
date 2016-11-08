from scrapy.selector import Selector
import scrapy
import html2text

class MarkovSpider(scrapy.Spider):
	name = 'markov'
	allowed_domains = ['http://www.soundofgrace.com/']
	start_urls =[
	'http://www.soundofgrace.com/piper81/100481m.htm'
	]

	def parse(self, response):
		sel = Selector(response)
		sample = s.xpath("//div[@id ='mw-content-text']/p[1]").extract()[0]

		converter = html2text.HTML2Text()
		converter.ignore_links = True
		print converter.handle(sample)
		

