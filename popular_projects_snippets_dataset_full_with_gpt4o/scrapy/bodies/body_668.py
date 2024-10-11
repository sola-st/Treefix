# Extracted from ./data/repos/scrapy/scrapy/utils/request.py
if crawler:
    implementation = crawler.settings.get(
        'REQUEST_FINGERPRINTER_IMPLEMENTATION'
    )
else:
    implementation = '2.6'
if implementation == '2.6':
    message = (
        '\'2.6\' is a deprecated value for the '
        '\'REQUEST_FINGERPRINTER_IMPLEMENTATION\' setting.\n'
        '\n'
        'It is also the default value. In other words, it is normal '
        'to get this warning if you have not defined a value for the '
        '\'REQUEST_FINGERPRINTER_IMPLEMENTATION\' setting. This is so '
        'for backward compatibility reasons, but it will change in a '
        'future version of Scrapy.\n'
        '\n'
        'See the documentation of the '
        '\'REQUEST_FINGERPRINTER_IMPLEMENTATION\' setting for '
        'information on how to handle this deprecation.'
    )
    warnings.warn(message, category=ScrapyDeprecationWarning, stacklevel=2)
    self._fingerprint = _request_fingerprint_as_bytes
elif implementation == '2.7':
    self._fingerprint = fingerprint
else:
    raise ValueError(
        f'Got an invalid value on setting '
        f'\'REQUEST_FINGERPRINTER_IMPLEMENTATION\': '
        f'{implementation!r}. Valid values are \'2.6\' (deprecated) '
        f'and \'2.7\'.'
    )
