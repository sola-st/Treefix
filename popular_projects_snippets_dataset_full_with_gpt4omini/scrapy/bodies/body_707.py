# Extracted from ./data/repos/scrapy/scrapy/commands/fetch.py
for key, values in headers.items():
    for value in values:
        self._print_bytes(prefix + b' ' + key + b': ' + value)
