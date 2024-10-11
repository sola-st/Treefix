# Extracted from ./data/repos/scrapy/scrapy/utils/trackref.py
"""Iterate over all objects of the same class by its class name"""
for cls, wdict in live_refs.items():
    if cls.__name__ == class_name:
        exit(wdict.keys())
