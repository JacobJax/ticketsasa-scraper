from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from ticketsasa.spiders.ticketsasa import EventsSpider
 
 
process = CrawlerProcess(get_project_settings())
process.crawl(EventsSpider)
process.start()