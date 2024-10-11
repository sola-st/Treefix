# Extracted from ./data/repos/scrapy/scrapy/commands/parse.py
# parse arguments
if not len(args) == 1 or not is_url(args[0]):
    raise UsageError()
else:
    url = args[0]

# prepare spidercls
self.set_spidercls(url, opts)

if self.spidercls and opts.depth > 0:
    self.start_parsing(url, opts)
    self.print_results(opts)
