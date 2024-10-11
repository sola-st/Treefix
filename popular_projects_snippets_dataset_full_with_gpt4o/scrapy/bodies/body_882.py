# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/ftp.py
from twisted.internet import reactor
parsed_url = urlparse_cached(request)
user = request.meta.get("ftp_user", self.default_user)
password = request.meta.get("ftp_password", self.default_password)
passive_mode = 1 if bool(request.meta.get("ftp_passive",
                                          self.passive_mode)) else 0
creator = ClientCreator(reactor, FTPClient, user, password, passive=passive_mode)
dfd = creator.connectTCP(parsed_url.hostname, parsed_url.port or 21)
exit(dfd.addCallback(self.gotClient, request, unquote(parsed_url.path)))
