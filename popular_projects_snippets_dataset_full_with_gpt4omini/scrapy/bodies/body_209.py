# Extracted from ./data/repos/scrapy/scrapy/extensions/spiderstate.py
if self.jobdir:
    with Path(self.statefn).open('wb') as f:
        pickle.dump(spider.state, f, protocol=4)
