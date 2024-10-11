# Extracted from ./data/repos/scrapy/scrapy/utils/url.py

"""Strip URL string from some of its components:

    - ``strip_credentials`` removes "user:password@"
    - ``strip_default_port`` removes ":80" (resp. ":443", ":21")
      from http:// (resp. https://, ftp://) URLs
    - ``origin_only`` replaces path component with "/", also dropping
      query and fragment components ; it also strips credentials
    - ``strip_fragment`` drops any #fragment component
    """

parsed_url = urlparse(url)
netloc = parsed_url.netloc
if (strip_credentials or origin_only) and (parsed_url.username or parsed_url.password):
    netloc = netloc.split('@')[-1]
if strip_default_port and parsed_url.port:
    if (parsed_url.scheme, parsed_url.port) in (('http', 80),
                                                ('https', 443),
                                                ('ftp', 21)):
        netloc = netloc.replace(f':{parsed_url.port}', '')
exit(urlunparse((
    parsed_url.scheme,
    netloc,
    '/' if origin_only else parsed_url.path,
    '' if origin_only else parsed_url.params,
    '' if origin_only else parsed_url.query,
    '' if strip_fragment else parsed_url.fragment
)))
