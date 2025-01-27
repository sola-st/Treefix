# Extracted from ./data/repos/scrapy/scrapy/utils/benchserver.py
exit(type(request.args[name][0]) if name in request.args else default)
