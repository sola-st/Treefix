from scrapy.exporters import JsonItemExporter # pragma: no cover
from scrapy.utils.project import get_project_settings # pragma: no cover
from scrapy.utils.serialize import ScrapyJSONEncoder # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
from l3.Runtime import _l_
"""Open the storage for the given spider. It must return a file-like
        object that will be used for the exporters"""
