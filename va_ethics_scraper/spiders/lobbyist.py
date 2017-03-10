# -*- coding: utf-8 -*-
import scrapy

from va_ethics_scraper.items import LobbyistScraperItem


class LobbyistSpider(scrapy.Spider):
    name = "lobbyist"
    allowed_domains = ["ethicssearch.dls.virginia.gov"]
    start_urls = ['http://ethicssearch.dls.virginia.gov/']

    def parse_post(self, response):
        rows = response.xpath('//span[@class="itemaction"]/../..')
        for row in rows:
            doc_url = row.xpath('td/a/@href').extract()[0]

            (_, _, l_name, principal, officer, _, submitted, status) = \
                [x.strip() for x in row.xpath('td/text()').extract()]

            yield LobbyistScraperItem(
                file_urls=[response.urljoin(doc_url)],
                lobbyist_name=l_name,
                principal=principal,
                officer=officer,
                submitted=submitted,
                status=status,
            )

    def parse(self, response):
        frmdata = {
            '__VIEWSTATE': '',
            '__VIEWSTATEGENERATOR': 'BBBC20B8',
            '__SCROLLPOSITIONX': '0',
            '__SCROLLPOSITIONY': '0',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            'hdnSelectedTab': '0',
            'lstYears': '2016-2017',
            'txtLobbyistName': '',
            'txtPrincipalName': '',
            'txtPrincipalOfficerName': '',
            'cmdSearch': 'Search',
            'lstYearCOI': '2017',
            'txtFirstName': '',
            'txtLastName': '',
            'txtAgency': '',
        }

        yield scrapy.FormRequest(
            response.url,
            formdata=frmdata,
            callback=self.parse_post
        )
