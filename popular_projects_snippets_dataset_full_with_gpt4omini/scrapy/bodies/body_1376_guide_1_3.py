from scrapy.exceptions import ScrapyDeprecationWarning # pragma: no cover
from scrapy.utils.project import get_project_settings # pragma: no cover

settings = get_project_settings() # pragma: no cover
settings.set('DUPEFILTER_DEBUG', True) # pragma: no cover
fingerprinter = 'mock_fingerprinter' # pragma: no cover
class Mock: pass # pragma: no cover
def job_dir(settings): return 'mock_job_dir' # pragma: no cover
class MockCls(Mock): # pragma: no cover
    def __init__(self, job_dir, debug, fingerprinter=None): # pragma: no cover
        if fingerprinter is not None: # pragma: no cover
            raise TypeError('Fingerprinter not supported') # pragma: no cover
        self.job_dir = job_dir # pragma: no cover
        self.debug = debug # pragma: no cover
cls = MockCls # pragma: no cover

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
