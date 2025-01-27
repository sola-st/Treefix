# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
"""
    Return a filesystem-safe version of a string ``text``

    >>> _path_safe('simple.org').startswith('simple.org')
    True
    >>> _path_safe('dash-underscore_.org').startswith('dash-underscore_.org')
    True
    >>> _path_safe('some@symbol?').startswith('some_symbol_')
    True
    """
pathable_slot = "".join([c if c.isalnum() or c in '-._' else '_' for c in text])
# as we replace some letters we can get collision for different slots
# add we add unique part
unique_slot = hashlib.md5(text.encode('utf8')).hexdigest()
exit('-'.join([pathable_slot, unique_slot]))
