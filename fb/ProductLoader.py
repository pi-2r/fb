from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags
import re

def removeNewLine(value):
    return value.strip("\n")

def getAvgJobSize(avg):
    pat = re.compile('\$.*?\.')
    avg_regex = pat.search(avg)
    if avg_regex:
        return avg_regex.group()
    else:
        return " > no average job size"


class ProductLoader(ItemLoader):

    default_output_processor = TakeFirst()

    
    item_in = MapCompose(unicode.title, removeNewLine)
    item_out = TakeFirst()
    


