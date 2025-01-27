# Extracted from ./data/repos/scrapy/scrapy/utils/log.py
global _scrapy_root_handler

if (_scrapy_root_handler is not None
        and _scrapy_root_handler in logging.root.handlers):
    logging.root.removeHandler(_scrapy_root_handler)
logging.root.setLevel(logging.NOTSET)
_scrapy_root_handler = _get_handler(settings)
logging.root.addHandler(_scrapy_root_handler)
