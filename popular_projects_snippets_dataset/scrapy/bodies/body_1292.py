# Extracted from ./data/repos/scrapy/scrapy/downloadermiddlewares/httpauth.py
usr = getattr(spider, 'http_user', '')
pwd = getattr(spider, 'http_pass', '')
if usr or pwd:
    self.auth = basic_auth_header(usr, pwd)
    if not hasattr(spider, 'http_auth_domain'):
        warnings.warn('Using HttpAuthMiddleware without http_auth_domain is deprecated and can cause security '
                      'problems if the spider makes requests to several different domains. http_auth_domain '
                      'will be set to the domain of the first request, please set it to the correct value '
                      'explicitly.',
                      category=ScrapyDeprecationWarning)
        self.domain_unset = True
    else:
        self.domain = spider.http_auth_domain
        self.domain_unset = False
