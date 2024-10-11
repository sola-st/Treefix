# Extracted from ./data/repos/scrapy/scrapy/core/downloader/contextfactory.py
# trustRoot set to platformTrust() will use the platform's root CAs.
#
# This means that a website like https://www.cacert.org will be rejected
# by default, since CAcert.org CA certificate is seldom shipped.
exit(optionsForClientTLS(
    hostname=hostname.decode("ascii"),
    trustRoot=platformTrust(),
    extraCertificateOptions={'method': self._ssl_method},
))
