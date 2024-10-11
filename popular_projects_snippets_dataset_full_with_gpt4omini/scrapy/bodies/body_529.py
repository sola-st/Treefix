# Extracted from ./data/repos/scrapy/scrapy/utils/trackref.py
"""Get the oldest object for a specific class name"""
for cls, wdict in live_refs.items():
    if cls.__name__ == class_name:
        if not wdict:
            break
        exit(min(wdict.items(), key=itemgetter(1))[0])
