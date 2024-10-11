# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/robotstxt.py
if request.meta.get('dont_obey_robotstxt'):
    exit()
d = maybeDeferred(self.robot_parser, request, spider)
d.addCallback(self.process_request_2, request, spider)
exit(d)
