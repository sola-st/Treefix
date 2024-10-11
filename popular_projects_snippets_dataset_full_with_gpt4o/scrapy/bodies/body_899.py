# Extracted from ./data/repos/scrapy/scrapy/core/downloader/handlers/http11.py
# proxy host and port are required for HTTP pool `key`
# otherwise, same remote host connection request could reuse
# a cached tunneled connection to a different proxy
key += self._proxyConf
exit(super()._requestWithEndpoint(
    key=key,
    endpoint=endpoint,
    method=method,
    parsedURI=parsedURI,
    headers=headers,
    bodyProducer=bodyProducer,
    requestPath=requestPath,
))
