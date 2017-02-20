# -*- coding: utf-8 -*-
import scrapy
from fb.ProductLoader import ProductLoader
from fb.items import item1
from scrapy_splash import SplashRequest


class fbcrawlSpider(scrapy.Spider):
    name = "fbcrawl"
    allowed_domains = ["facebook.com"]
    domain = "https://www.facebook.com"
    start_urls = [
        'https://www.facebook.com' ]

    # 'https://www.facebook.com/groups/velaansandhai',
    # 'https://www.facebook.com/groups/farmerjunction'

    username = ''
    password = ''

    def __init__(self, username, password):

        if username != '':
            self.username = username
        if password != '':
            self.password = password


    def start_requests(self):
        script = """
                function main(splash)
                local url = splash.args.url
                assert(splash:go(url))
                local form = splash:select('#login_form')
                local values = assert(form:form_values())
                values.email = "{0}"
                values.pass = "{1}"
                assert(form:fill(values))
                assert(form:submit())
                splash:wait(4)

                function wait_for(splash, condition)
                    while not condition() do
                        splash:wait(0.05)
                    end
                end

                wait_for(splash, function()
                    return splash:evaljs("document.querySelector('[id^=profile_pic_header]') != null") end)

                return {{
                cookies = splash:get_cookies(),
                html = splash:html(),
                png = splash:png(),
                har = splash:har(),
                }}
                end
                """.format(self.username,self.password)
        #print script
        for url in self.start_urls:
            print url
            req =  SplashRequest(url, self.parse,
                                endpoint='execute',
                                args={'lua_source': script},
                                )
            req.meta['splash']['session_id'] = 'foo'
            yield req

    def parse(self, response):

        script = """
                        function main(splash)
                        splash:init_cookies(splash.args.cookies)
                        local url = splash.args.url
                        assert(splash:go(url))

                        function wait_for(splash, condition)
                            while not condition() do
                                splash:wait(0.05)
                            end
                        end

                        wait_for(splash, function()
                            return splash:evaljs("document.querySelector('[id^=profile_pic_header]') != null") end)

                        return {{
                        cookies = splash:get_cookies(),
                        html = splash:html(),
                        png = splash:png(),
                        har = splash:har(),
                        }}
                        end
                        """

        req =  SplashRequest('https://www.facebook.com/groups/velaansandhai', self.parseVSPosts,
                            endpoint='execute',
                             args={'lua_source': script},
                            )
        req.meta['splash']['session_id'] = 'foo'
        yield req

    def parseVSPosts(self, response):
        print response.body
