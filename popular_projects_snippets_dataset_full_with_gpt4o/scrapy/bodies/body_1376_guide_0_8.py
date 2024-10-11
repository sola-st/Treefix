from scrapy.utils.project import get_project_settings # pragma: no cover
from scrapy.exceptions import ScrapyDeprecationWarning # pragma: no cover
import warnings # pragma: no cover

settings = get_project_settings() # pragma: no cover
settings.set('DUPEFILTER_DEBUG', True) # pragma: no cover
fingerprinter = type('MockFingerprinter', (object,), {})() # pragma: no cover
def job_dir(settings): return '/some/path' # pragma: no cover
class cls: # pragma: no cover
    def __init__(self, job_dir, debug, fingerprinter=None): # pragma: no cover
        if fingerprinter is None: # pragma: no cover
            raise TypeError('fingerprinter is required') # pragma: no cover
        self.job_dir = job_dir # pragma: no cover
        self.debug = debug # pragma: no cover
        self.fingerprinter = fingerprinter # pragma: no cover
    def from_settings(cls, settings): pass # pragma: no cover
def warn(message, warning_cls): # pragma: no cover
    warnings.warn(message, warning_cls) # pragma: no cover
aux = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/dupefilters.py
from l3.Runtime import _l_
debug = settings.getbool('DUPEFILTER_DEBUG')
_l_(16095)
try:
    _l_(16102)

    aux = cls(job_dir(settings), debug, fingerprinter=fingerprinter)
    _l_(16096)
    exit(aux)
except TypeError:
    _l_(16101)

    warn(
        "RFPDupeFilter subclasses must either modify their '__init__' "
        "method to support a 'fingerprinter' parameter or reimplement "
        "the 'from_settings' class method.",
        ScrapyDeprecationWarning,
    )
    _l_(16097)
    result = cls(job_dir(settings), debug)
    _l_(16098)
    result.fingerprinter = fingerprinter
    _l_(16099)
    aux = result
    _l_(16100)
    exit(aux)
