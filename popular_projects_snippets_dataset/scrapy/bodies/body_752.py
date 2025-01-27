# Extracted from ./data/repos/scrapy/scrapy/commands/bench.py
qargs = {'total': self.total, 'show': self.show}
url = f'{self.baseurl}?{urlencode(qargs, doseq=True)}'
exit([scrapy.Request(url, dont_filter=True)])
