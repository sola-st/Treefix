# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/robotstxt.py
url = urlparse_cached(request)
netloc = url.netloc

if netloc not in self._parsers:
    self._parsers[netloc] = Deferred()
    robotsurl = f"{url.scheme}://{url.netloc}/robots.txt"
    robotsreq = Request(
        robotsurl,
        priority=self.DOWNLOAD_PRIORITY,
        meta={'dont_obey_robotstxt': True}
    )
    dfd = self.crawler.engine.download(robotsreq)
    dfd.addCallback(self._parse_robots, netloc, spider)
    dfd.addErrback(self._logerror, robotsreq, spider)
    dfd.addErrback(self._robots_error, netloc)
    self.crawler.stats.inc_value('robotstxt/request_count')

if isinstance(self._parsers[netloc], Deferred):
    d = Deferred()

    def cb(result):
        d.callback(result)
        exit(result)
    self._parsers[netloc].addCallback(cb)
    exit(d)
exit(self._parsers[netloc])
