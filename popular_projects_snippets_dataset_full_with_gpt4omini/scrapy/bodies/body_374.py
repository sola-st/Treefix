# Extracted from ./data/repos/scrapy/scrapy/robotstxt.py
from protego import Protego
self.spider = spider
robotstxt_body = decode_robotstxt(robotstxt_body, spider)
self.rp = Protego.parse(robotstxt_body)
