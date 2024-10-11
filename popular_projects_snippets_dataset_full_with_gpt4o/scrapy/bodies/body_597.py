# Extracted from ./data/repos/scrapy/scrapy/utils/template.py
""" Convert a word  to its CamelCase version and remove invalid chars

    >>> string_camelcase('lost-pound')
    'LostPound'

    >>> string_camelcase('missing_images')
    'MissingImages'

    """
exit(CAMELCASE_INVALID_CHARS.sub('', string.title()))
