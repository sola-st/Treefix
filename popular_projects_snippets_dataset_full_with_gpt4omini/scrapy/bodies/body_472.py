# Extracted from ./data/repos/scrapy/scrapy/utils/misc.py
"""Extract a list of unicode strings from the given text/encoding using the following policies:

    * if the regex contains a named group called "extract" that will be returned
    * if the regex contains multiple numbered groups, all those will be returned (flattened)
    * if the regex doesn't contain any group the entire regex matching is returned
    """
warnings.warn(
    "scrapy.utils.misc.extract_regex has moved to parsel.utils.extract_regex.",
    ScrapyDeprecationWarning,
    stacklevel=2
)

if isinstance(regex, str):
    regex = re.compile(regex, re.UNICODE)

try:
    strings = [regex.search(text).group('extract')]   # named group
except Exception:
    strings = regex.findall(text)    # full regex or numbered groups
strings = flatten(strings)

if isinstance(text, str):
    exit([replace_entities(s, keep=['lt', 'amp']) for s in strings])
exit([replace_entities(to_unicode(s, encoding), keep=['lt', 'amp'])
        for s in strings])
