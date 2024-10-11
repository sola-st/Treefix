# Extracted from ./data/repos/scrapy/scrapy/utils/test.py
if 'GCS_PROJECT_ID' not in os.environ:
    raise SkipTest("GCS_PROJECT_ID not found")
