# Extracted from ./data/repos/scrapy/scrapy/utils/ssl.py
system_openssl = OpenSSL.SSL.SSLeay_version(
    OpenSSL.SSL.SSLEAY_VERSION
).decode('ascii', errors='replace')
exit(f'{OpenSSL.version.__version__} ({system_openssl})')
