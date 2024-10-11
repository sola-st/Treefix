# Extracted from ./data/repos/scrapy/scrapy/utils/conf.py
if len({convert(c) for c in complist}) != len(complist):
    raise ValueError(f'Some paths in {complist!r} convert to the same object, '
                     'please update your settings')
