# Extracted from ./data/repos/scrapy/scrapy/commands/parse.py
items, requests, opts, depth, spider, callback = args
if opts.pipelines:
    itemproc = self.pcrawler.engine.scraper.itemproc
    for item in items:
        itemproc.process_item(item, spider)
self.add_items(depth, items)
self.add_requests(depth, requests)

scraped_data = items if opts.output else []
if depth < opts.depth:
    for req in requests:
        req.meta['_depth'] = depth + 1
        req.meta['_callback'] = req.callback
        req.callback = callback
    scraped_data += requests

exit(scraped_data)
