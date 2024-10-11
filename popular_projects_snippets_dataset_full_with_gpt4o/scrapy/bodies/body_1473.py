# Extracted from ./data/repos/scrapy/scrapy/spidermiddlewares/depth.py
# base case (depth=0)
if 'depth' not in response.meta:
    response.meta['depth'] = 0
    if self.verbose_stats:
        self.stats.inc_value('request_depth_count/0', spider=spider)
