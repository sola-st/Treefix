# Extracted from ./data/repos/scrapy/scrapy/robotstxt.py
from urllib.robotparser import RobotFileParser
self.spider = spider
robotstxt_body = decode_robotstxt(robotstxt_body, spider, to_native_str_type=True)
self.rp = RobotFileParser()
self.rp.parse(robotstxt_body.splitlines())
