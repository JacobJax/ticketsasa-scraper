import scrapy

class EventsSpider(scrapy.Spider): 
   name = "ticketsasa"

   start_urls = [
      "https://www.ticketsasa.com/events"
   ]

   def parse(self, response):
      
      posts = response.css('.tkt-evt')
      for post in posts:
         yield {
            'title': post.css('.evt-info h3 a span::text').get(),
            'link': f"https://www.ticketsasa.com{post.css('.evt-info h3 a::attr(href)').get()}",
            'time': f"{post.css('.date-box .day::text').get()} {post.css('.date-box .date::text').get()} {post.css('.date-box .month::text').get()}"
         }
      
      # next_page = response.css('.pagination li a::attr(href)')[1].get()
      # if next_page is not None:
      #    next_page = response.urljoin(next_page)
      #    yield scrapy.Request(next_page, callback=self.parse)