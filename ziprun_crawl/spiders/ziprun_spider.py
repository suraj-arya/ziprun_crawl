from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from ziprun_crawl.items import ZiprunCrawlItem


class ZiprunSpider(CrawlSpider):

    name = 'ziprun'
    start_urls = ['https://www.zomato.com/ncr',
                  'https://www.zomato.com/ncr/restaurants',
                  'https://www.zomato.com/ncr/restaurants?page=2']
    rules = [Rule(SgmlLinkExtractor(allow=[r'/ncr/restaurants?page=\d*']), follow=True),
             Rule(SgmlLinkExtractor(allow=[r'/ncr/[-\w?/#%]+']), follow=True, callback='parse_url'),
             Rule(SgmlLinkExtractor(allow=[r'/ncr/restaurants?category=\d*&page=\d*[%/\w?&#]*']), follow=True),
             Rule(SgmlLinkExtractor(allow=[r'/ncr/restaurants/\w*?page=\d*[/\w?&#%]*']), follow=True),
             Rule(SgmlLinkExtractor(allow=[r'zomato.com/[/?&\w#%]+']), callback='parse_url')]

    def parse_url(self, response):

        hxs = HtmlXPathSelector(response)
        item = ZiprunCrawlItem()

        item['restuarant_name'] = hxs.select('/html/body/div[3]/div[4]/div/div/div[2]/div/div/div[1]/div/'
                                             'div[2]/div/h1/a/span/node()').extract()
        item['phone'] = hxs.select('//*[@id="phoneNoString"]/div/span/span/span/node()').extract()
        item['delivery'] = hxs.select('//*[@id="mainframe"]/div[1]/div/div[1]/'
                                      'div[3]/div[6]/div[2]/div/div[1]/div[2]/node()').extract()
        item['reviews'] = hxs.select('//*[@id="selectors"]/li[3]/a/span/node()').extract()
        item['checkin'] = hxs.select('//*[@id="mainframe"]/div[1]/div/'
                                     'div[1]/div[3]/div[6]/div[2]/div/div[2]/div[2]/node()').extract()
        item['rating'] = hxs.select('/html/body/div[3]/div[4]/div/div/div[2]/div/'
                                    'div/div[1]/div/div[3]/div/div/div/div[1]/node()').extract()
        item['cuisines'] = hxs.select('//*[@id="mainframe"]/div[1]/div/div[1]/div[3]'
                                      '/div[1]/div[2]/div[1]/div/div/node()').extract()
        item['establishment'] = hxs.select('//*[@id="mainframe"]/div[1]/'
                                           'div/div[1]/div[3]/div[2]/div/div/a[2]/node()').extract()
        item['address'] = hxs.select('//*[@id="mainframe"]/div[1]/div/div[1]/div[1]/div[2]/div/div[1]/a/b/node()').extract()
        item['bookmarks'] = hxs.select('//*[@id="wtt_count"]/node()').extract()

        if item['restuarant_name'] and item['phone'] and item['address']:

            return item

        return None