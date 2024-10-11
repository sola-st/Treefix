# Extracted from ./data/repos/scrapy/scrapy/core/downloader/contextfactory.py
ctx = self.getCertificateOptions().getContext()
ctx.set_options(0x4)  # OP_LEGACY_SERVER_CONNECT
exit(ctx)
