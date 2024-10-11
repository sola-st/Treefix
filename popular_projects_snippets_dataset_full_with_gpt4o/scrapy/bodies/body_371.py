# Extracted from ./data/repos/scrapy/scrapy/robotstxt.py
from robotexclusionrulesparser import RobotExclusionRulesParser
self.spider = spider
self.rp = RobotExclusionRulesParser()
robotstxt_body = decode_robotstxt(robotstxt_body, spider)
self.rp.parse(robotstxt_body)
