# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import XMLFeedSpider
from scrapeXML.items import ScrapexmlItem

class SxmlSpider(XMLFeedSpider):
    name = 'sXML'
    start_urls = ['http://www-db.deis.unibo.it/courses/TW/DOCS/w3schools/xml/simple.xml']
    itertag='food'


    def parse_node(self, response, node):
        items=ScrapexmlItem()
        items['name']=node.css('name::text').get()
        items['price']=node.css('price::text').get()
        items['desc']=node.css('description::text').get()
        

        #items['name']=node.xpath('//food/name/text()').get()
        #items['price']=node.xpath('//food/price/text()').get()
        #items['desc']=node.xpath('//food/description/text()').get()
        print('\n\n\n')
        return items

'''
<breakfast_menu>
<food>
<name>Belgian Waffles</name>
<price>$5.95</price>
<description>
Two of our famous Belgian Waffles with plenty of real maple syrup
</description>
<calories>650</calories>
</food>
<food>
<name>Strawberry Belgian Waffles</name>
<price>$7.95</price>
<description>
Light Belgian waffles covered with strawberries and whipped cream
</description>
<calories>900</calories>
</food>
<food>
<name>Berry-Berry Belgian Waffles</name>
<price>$8.95</price>
<description>
Light Belgian waffles covered with an assortment of fresh berries and whipped cream
</description>
<calories>900</calories>
</food>
<food>
<name>French Toast</name>
<price>$4.50</price>
<description>
Thick slices made from our homemade sourdough bread
</description>
<calories>600</calories>
</food>
<food>
<name>Homestyle Breakfast</name>
<price>$6.95</price>
<description>
Two eggs, bacon or sausage, toast, and our ever-popular hash browns
</description>
<calories>950</calories>
</food>
</breakfast_menu>
'''