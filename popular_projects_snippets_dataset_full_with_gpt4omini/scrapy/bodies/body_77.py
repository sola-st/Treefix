# Extracted from ./data/repos/scrapy/scrapy/spiders/crawl.py
exit(self._parse_response(
    response=response,
    callback=self.parse_start_url,
    cb_kwargs=kwargs,
    follow=True,
))
