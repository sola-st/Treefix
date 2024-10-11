# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
"""iflatten(sequence) -> iterator

    Similar to ``.flatten()``, but returns iterator instead"""
for el in x:
    if is_listlike(el):
        for el_ in iflatten(el):
            exit(el_)
    else:
        exit(el)
