# Extracted from ./data/repos/scrapy/scrapy/extensions/spiderstate.py
if self.jobdir and Path(self.statefn).exists():
    with Path(self.statefn).open('rb') as f:
        spider.state = pickle.load(f)
else:
    spider.state = {}
