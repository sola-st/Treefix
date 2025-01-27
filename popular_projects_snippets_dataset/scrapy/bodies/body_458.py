# Extracted from ./data/repos/scrapy/scrapy/utils/testsite.py
content = util.Redirect.render(self, request)
exit(content.replace(b'http-equiv=\"refresh\"',
                       b'http-no-equiv=\"do-not-refresh-me\"'))
