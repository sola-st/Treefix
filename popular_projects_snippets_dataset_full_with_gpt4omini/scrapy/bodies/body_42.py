# Extracted from ./data/repos/scrapy/scrapy/cmdline.py
try:
    func(*a, **kw)
except UsageError as e:
    if str(e):
        parser.error(str(e))
    if e.print_help:
        parser.print_help()
    sys.exit(2)
