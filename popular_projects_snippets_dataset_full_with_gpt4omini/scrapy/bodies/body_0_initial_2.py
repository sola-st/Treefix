import warnings # pragma: no cover
from scrapy.exceptions import ScrapyDeprecationWarning # pragma: no cover
import common # pragma: no cover

ScrapyDeprecationWarning = ScrapyDeprecationWarning # pragma: no cover
common = type('MockCommon', (object,), {'wrap_loader_context': lambda f, c: f'wrapped({c})'})() # pragma: no cover
function = lambda x: f'function called with {x}' # pragma: no cover
context = 'pre-loaded context' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/loader/common.py
from l3.Runtime import _l_
"""Wrap functions that receive loader_context to contain the context
    "pre-loaded" and expose a interface that receives only one argument
    """
warnings.warn(
    "scrapy.loader.common.wrap_loader_context has moved to a new library."
    "Please update your reference to itemloaders.common.wrap_loader_context",
    ScrapyDeprecationWarning,
    stacklevel=2
)
_l_(7925)
aux = common.wrap_loader_context(function, context)
_l_(7926)

exit(aux)
