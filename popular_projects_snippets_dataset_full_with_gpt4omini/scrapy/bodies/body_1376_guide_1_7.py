from scrapy.exceptions import ScrapyDeprecationWarning # pragma: no cover

class Mock: pass # pragma: no cover
def job_dir(settings): return 'mock_job_dir' # pragma: no cover
class cls(Mock): # pragma: no cover
    def __init__(self, job_dir, debug, fingerprinter=None): # pragma: no cover
        self.job_dir = job_dir # pragma: no cover
        self.debug = debug # pragma: no cover
        self.fingerprinter = fingerprinter # pragma: no cover
    @classmethod # pragma: no cover
    def from_settings(cls, settings): return cls(job_dir(settings), settings.getbool('DUPEFILTER_DEBUG')) # pragma: no cover
settings = type('MockSettings', (object,), {'getbool': lambda self, key: False})() # pragma: no cover
debug = settings.getbool('DUPEFILTER_DEBUG') # pragma: no cover
fingerprinter = 'mock_fingerprinter' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/dupefilters.py
from l3.Runtime import _l_
debug = settings.getbool('DUPEFILTER_DEBUG')
_l_(4743)
try:
    _l_(4750)

    aux = cls(job_dir(settings), debug, fingerprinter=fingerprinter)
    _l_(4744)
    exit(aux)
except TypeError:
    _l_(4749)

    warn(
        "RFPDupeFilter subclasses must either modify their '__init__' "
        "method to support a 'fingerprinter' parameter or reimplement "
        "the 'from_settings' class method.",
        ScrapyDeprecationWarning,
    )
    _l_(4745)
    result = cls(job_dir(settings), debug)
    _l_(4746)
    result.fingerprinter = fingerprinter
    _l_(4747)
    aux = result
    _l_(4748)
    exit(aux)
