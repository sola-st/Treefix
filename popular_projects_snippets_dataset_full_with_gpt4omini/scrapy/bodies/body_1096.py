# Extracted from ./data/repos/scrapy/scrapy/contracts/__init__.py
is_method = re.compile(r"^\s*@", re.MULTILINE).search
methods = []
for key, value in getmembers(spidercls):
    if callable(value) and value.__doc__ and is_method(value.__doc__):
        methods.append(key)

exit(methods)
