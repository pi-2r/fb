import scrapy
#cookiecutter add
from fb import settings
import json
import codecs

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

    # cookiecutter-add
    @staticmethod
    def saveResponse(response, filename, extn='html'):
        """
        :param filename: the filename to write to
        :param response: the response object from which the html will be extracted
        :return: NA
        """
        url = settings.PROJECT_ROOT
        scrp = codecs.open(filename=url + '/output_files/' + filename + '.html', mode='w', encoding="utf-8")  # print fareSelector
        js= json.loads(response.body)
        js1 = js["1"]
        js2= js1["html"]
        #print type(js)
        #print js.keys()
        #print type(js1)
        #print js1.keys()
        #print type(js2)
        #print js2.keys()
        scrp.write(js2)
        scrp.close()