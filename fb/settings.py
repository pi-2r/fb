# -*- coding: utf-8 -*-

# Scrapy settings for fb project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'fb'

SPIDER_MODULES = ['fb.spiders']
NEWSPIDER_MODULE = 'fb.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'fb (+http://www.yourdomain.com)'


FEED_FORMAT= 'csv'
FEED_URI= 'fb_output.csv'
#LOG_LEVEL = 'ERROR'
CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 2

FEED_EXPORTERS = {
    'csv': 'common.exporters.feedexport.CSVkwItemExporter'
}

# By specifying the fields to export, the CSV export honors the order
# rath'er than using a random order.
EXPORT_FIELDS = [

    'item'

]

#DOWNLOADER_MIDDLEWARES = {
#'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#'scrapetest.middlewares.ProxyMiddleware': 100
#}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
SPLASH_COOKIES_DEBUG = True
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPLASH_URL = 'http://localhost:8050/'