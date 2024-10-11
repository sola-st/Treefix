# Extracted from ./data/repos/scrapy/scrapy/commands/parse.py
def callback(response, **cb_kwargs):
    # memorize first request
    if not self.first_response:
        self.first_response = response

    # determine real callback
    cb = response.meta['_callback']
    if not cb:
        if opts.callback:
            cb = opts.callback
        elif opts.rules and self.first_response == response:
            cb = self.get_callback_from_rules(spider, response)

            if not cb:
                logger.error('Cannot find a rule that matches %(url)r in spider: %(spider)s',
                             {'url': response.url, 'spider': spider.name})
                exit()
        else:
            cb = 'parse'

    if not callable(cb):
        cb_method = getattr(spider, cb, None)
        if callable(cb_method):
            cb = cb_method
        else:
            logger.error('Cannot find callback %(callback)r in spider: %(spider)s',
                         {'callback': cb, 'spider': spider.name})
            exit()

            # parse items and requests
    depth = response.meta['_depth']

    d = self.run_callback(response, cb, cb_kwargs)
    d.addCallback(self._get_items_and_requests, opts, depth, spider, callback)
    d.addCallback(self.scraped_data)
    exit(d)

# update request meta if any extra meta was passed through the --meta/-m opts.
if opts.meta:
    request.meta.update(opts.meta)

# update cb_kwargs if any extra values were was passed through the --cbkwargs option.
if opts.cbkwargs:
    request.cb_kwargs.update(opts.cbkwargs)

request.meta['_depth'] = 1
request.meta['_callback'] = request.callback
request.callback = callback
exit(request)
