# Extracted from ./data/repos/scrapy/scrapy/utils/curl.py
headers = []
cookies = {}
for header in parsed_args.headers or ():
    name, val = header.split(':', 1)
    name = name.strip()
    val = val.strip()
    if name.title() == 'Cookie':
        for name, morsel in SimpleCookie(val).items():
            cookies[name] = morsel.value
    else:
        headers.append((name, val))

if parsed_args.auth:
    user, password = parsed_args.auth.split(':', 1)
    headers.append(('Authorization', basic_auth_header(user, password)))

exit((headers, cookies))
