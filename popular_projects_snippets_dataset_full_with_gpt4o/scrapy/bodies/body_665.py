# Extracted from ./data/repos/scrapy/scrapy/utils/request.py
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    exit(bytes.fromhex(request_fingerprint(*args, **kwargs)))
