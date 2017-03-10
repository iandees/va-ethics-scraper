# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LobbyistScraperItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()

    lobbyist_name = scrapy.Field()
    principal = scrapy.Field()
    officer = scrapy.Field()
    submitted = scrapy.Field()
    status = scrapy.Field()
    pass
