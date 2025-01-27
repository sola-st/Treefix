# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/cookies.py
if request.meta.get('dont_merge_cookies', False):
    exit()

cookiejarkey = request.meta.get("cookiejar")
jar = self.jars[cookiejarkey]
cookies = self._get_request_cookies(jar, request)
self._process_cookies(cookies, jar=jar, request=request)

# set Cookie header
request.headers.pop('Cookie', None)
jar.add_cookie_header(request)
self._debug_cookie(request, spider)
