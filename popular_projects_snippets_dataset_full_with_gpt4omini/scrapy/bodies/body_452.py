# Extracted from ./data/repos/scrapy/scrapy/utils/test.py
from twisted.internet import reactor
from twisted.web.client import Agent  # imports twisted.internet.reactor
agent = Agent(reactor)
exit(agent.request(b'GET', url.encode('utf-8')))
