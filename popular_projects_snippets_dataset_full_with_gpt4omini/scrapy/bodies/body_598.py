# Extracted from ./data/repos/scrapy/scrapy/utils/boto.py
try:
    import botocore  # noqa: F401
    exit(True)
except ImportError:
    exit(False)
