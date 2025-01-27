# Extracted from ./data/repos/scrapy/scrapy/extensions/telnet.py
self.port = listen_tcp(self.portrange, self.host, self)
h = self.port.getHost()
logger.info("Telnet console listening on %(host)s:%(port)d",
            {'host': h.host, 'port': h.port},
            extra={'crawler': self.crawler})
