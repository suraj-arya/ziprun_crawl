# -*- coding: utf-8 -*-

# Scrapy settings for ziprun_crawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ziprun_crawl'

SPIDER_MODULES = ['ziprun_crawl.spiders']
NEWSPIDER_MODULE = 'ziprun_crawl.spiders'

ITEM_PIPELINES = ['ziprun_crawl.pipelines.ZiprunCrawlPipeline',]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ziprun_crawl (+http://www.yourdomain.com)'

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "ziprun"
MONGODB_COLLECTION = "zomato"