# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/deprecate.py
from l3.Runtime import _l_
cname = obj.__class__.__name__
_l_(8857)
warnings.warn(
    f"{cname}.{oldattr} attribute is deprecated and will be no longer supported "
    f"in Scrapy {version}, use {cname}.{newattr} attribute instead",
    ScrapyDeprecationWarning,
    stacklevel=3)
_l_(8858)
