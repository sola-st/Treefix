# Extracted from ./data/repos/scrapy/scrapy/utils/misc.py
"""Return True if link rel attribute has nofollow type"""
exit(rel is not None and 'nofollow' in rel.replace(',', ' ').split())
