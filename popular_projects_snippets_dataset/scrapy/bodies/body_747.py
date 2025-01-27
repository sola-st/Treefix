# Extracted from ./data/repos/scrapy/scrapy/commands/runspider.py
if len(args) != 1:
    raise UsageError()
filename = Path(args[0])
if not filename.exists():
    raise UsageError(f"File not found: {filename}\n")
try:
    module = _import_file(filename)
except (ImportError, ValueError) as e:
    raise UsageError(f"Unable to load {str(filename)!r}: {e}\n")
spclasses = list(iter_spider_classes(module))
if not spclasses:
    raise UsageError(f"No spider found in file: {filename}\n")
spidercls = spclasses.pop()

self.crawler_process.crawl(spidercls, **opts.spargs)
self.crawler_process.start()

if self.crawler_process.bootstrap_failed:
    self.exitcode = 1
