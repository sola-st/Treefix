# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/cookies.py
if self.debug:
    cl = [to_unicode(c, errors='replace')
          for c in request.headers.getlist('Cookie')]
    if cl:
        cookies = "\n".join(f"Cookie: {c}\n" for c in cl)
        msg = f"Sending cookies to: {request}\n{cookies}"
        logger.debug(msg, extra={'spider': spider})
