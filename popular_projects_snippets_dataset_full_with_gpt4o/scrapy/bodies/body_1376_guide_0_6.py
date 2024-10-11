import warnings # pragma: no cover
from types import SimpleNamespace as Mock # pragma: no cover

class settings: # pragma: no cover
    @staticmethod # pragma: no cover
    def getbool(key): # pragma: no cover
        return True # pragma: no cover
class ScrapyDeprecationWarning(Warning): # pragma: no cover
    pass # pragma: no cover
def job_dir(settings): # pragma: no cover
    return '/mock/job/dir' # pragma: no cover
fingerprinter = Mock() # pragma: no cover
def warn(message, category): # pragma: no cover
    warnings.warn(message, category) # pragma: no cover
class cls: # pragma: no cover
    def __init__(self, job_dir, debug, fingerprinter=None): # pragma: no cover
        if fingerprinter is None: # pragma: no cover
            raise TypeError # pragma: no cover
        self.job_dir = job_dir # pragma: no cover
        self.debug = debug # pragma: no cover
        self.fingerprinter = fingerprinter # pragma: no cover
    @classmethod # pragma: no cover
    def from_settings(cls, settings): # pragma: no cover
        return cls(job_dir(settings), settings.getbool('DUPEFILTER_DEBUG'), fingerprinter=None) # pragma: no cover

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
