# Extracted from ./data/repos/scrapy/scrapy/utils/url.py
exit(bool(
    re.match(
        r'''
            ^
            (
                [a-z]:\\
                | \\\\
            )
            ''',
        string,
        flags=re.IGNORECASE | re.VERBOSE,
    )
))
