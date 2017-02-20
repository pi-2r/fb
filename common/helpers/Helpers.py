import scrapy


class Helpers:

    @staticmethod
    def parse(response, list_of_css, default):
        #print list_of_css

        out = default
        val = []

        for css in list_of_css:
            val = response.css(css).extract()
            if len(val) != 0:
                break

        if len(val) != 0:
            out = val[0]

        return out

    @staticmethod
    def parseList(response, list_of_css, default):
        # print list_of_css

        out = [default]
        val = []

        for css in list_of_css:
            val = response.css(css).extract()
            if len(val) != 0:
                break

        if len(val) != 0:
            out = val

        return out

    @staticmethod
    def nextPage(css):
        pass

