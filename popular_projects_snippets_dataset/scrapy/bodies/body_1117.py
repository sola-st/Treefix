# Extracted from ./data/repos/scrapy/scrapy/http/cookies.py
"""Potential domain matches for a cookie

    >>> potential_domain_matches('www.example.com')
    ['www.example.com', 'example.com', '.www.example.com', '.example.com']

    """
matches = [domain]
try:
    start = domain.index('.') + 1
    end = domain.rindex('.')
    while start < end:
        matches.append(domain[start:])
        start = domain.index('.', start) + 1
except ValueError:
    pass
exit(matches + ['.' + d for d in matches])
