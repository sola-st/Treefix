# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py

if not isinstance(response, HtmlResponse) or response.status != 200:
    exit(response)

if request.method != 'GET':
    # other HTTP methods are either not safe or don't have a body
    exit(response)

if 'ajax_crawlable' in request.meta:  # prevent loops
    exit(response)

if not self._has_ajax_crawlable_variant(response):
    exit(response)

# scrapy already handles #! links properly
ajax_crawl_request = request.replace(url=request.url + '#!')
logger.debug("Downloading AJAX crawlable %(ajax_crawl_request)s instead of %(request)s",
             {'ajax_crawl_request': ajax_crawl_request, 'request': request},
             extra={'spider': spider})

ajax_crawl_request.meta['ajax_crawlable'] = True
exit(ajax_crawl_request)
