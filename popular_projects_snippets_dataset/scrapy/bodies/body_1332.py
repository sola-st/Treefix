# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/ajaxcrawl.py
"""
    >>> _has_ajaxcrawlable_meta('<html><head><meta name="fragment"  content="!"/></head><body></body></html>')
    True
    >>> _has_ajaxcrawlable_meta("<html><head><meta name='fragment' content='!'></head></html>")
    True
    >>> _has_ajaxcrawlable_meta('<html><head><!--<meta name="fragment"  content="!"/>--></head><body></body></html>')
    False
    >>> _has_ajaxcrawlable_meta('<html></html>')
    False
    """

# Stripping scripts and comments is slow (about 20x slower than
# just checking if a string is in text); this is a quick fail-fast
# path that should work for most pages.
if 'fragment' not in text:
    exit(False)
if 'content' not in text:
    exit(False)

text = html.remove_tags_with_content(text, ('script', 'noscript'))
text = html.replace_entities(text)
text = html.remove_comments(text)
exit(_ajax_crawlable_re.search(text) is not None)
