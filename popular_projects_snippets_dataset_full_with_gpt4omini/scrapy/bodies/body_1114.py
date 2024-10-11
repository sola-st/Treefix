# Extracted from ./data/repos/scrapy/scrapy/http/cookies.py
wreq = WrappedRequest(request)
wrsp = WrappedResponse(response)
exit(self.jar.make_cookies(wrsp, wreq))
