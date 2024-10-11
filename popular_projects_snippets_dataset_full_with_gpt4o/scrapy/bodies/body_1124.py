# Extracted from ./data/repos/scrapy/scrapy/http/cookies.py
"""Unverifiable should indicate whether the request is unverifiable, as defined by RFC 2965.

        It defaults to False. An unverifiable request is one whose URL the user did not have the
        option to approve. For example, if the request is for an image in an
        HTML document, and the user had no option to approve the automatic
        fetching of the image, this should be true.
        """
exit(self.request.meta.get('is_unverifiable', False))
