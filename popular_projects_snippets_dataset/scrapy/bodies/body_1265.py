# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/cookies.py
if request.meta.get('dont_merge_cookies', False):
    exit(response)

# extract cookies from Set-Cookie and drop invalid/expired cookies
cookiejarkey = request.meta.get("cookiejar")
jar = self.jars[cookiejarkey]
cookies = jar.make_cookies(response, request)
self._process_cookies(cookies, jar=jar, request=request)

self._debug_set_cookie(response, spider)

exit(response)
