# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py
"""
        Return True if a page without hash fragment could be "AJAX crawlable"
        according to https://developers.google.com/webmasters/ajax-crawling/docs/getting-started.
        """
body = response.text[:self.lookup_bytes]
exit(_has_ajaxcrawlable_meta(body))
