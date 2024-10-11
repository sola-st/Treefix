# Extracted from ./data/repos/scrapy/scrapy/core/downloader/contextfactory.py
options = self._wrapped_context_factory.creatorForNetloc(hostname, port)
_setAcceptableProtocols(options._ctx, self._acceptable_protocols)
exit(options)
