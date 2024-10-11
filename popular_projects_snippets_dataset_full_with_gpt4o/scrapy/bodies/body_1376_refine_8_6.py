from warnings import warn # pragma: no cover
from scrapy.exceptions import ScrapyDeprecationWarning # pragma: no cover

settings = type('MockSettings', (object,), {'getbool': lambda self, key: False})() # pragma: no cover
cls = type('MockClass', (object,), {'__init__': lambda self, job_dir, debug, fingerprinter=None: None, 'from_settings': classmethod(lambda cls, settings: None)}) # pragma: no cover
job_dir = lambda settings: '/mock/job/dir' # pragma: no cover
fingerprinter = type('MockFingerprinter', (object,), {})() # pragma: no cover

import warnings # pragma: no cover
from scrapy.settings import Settings # pragma: no cover
from scrapy.utils.job import job_dir # pragma: no cover
from scrapy.exceptions import ScrapyDeprecationWarning # pragma: no cover

settings = Settings({'DUPEFILTER_DEBUG': True}) # pragma: no cover
cls = type('MockFilterClass', (object,), {'__init__': lambda self, job_dir, debug, fingerprinter=None: setattr(self, 'fingerprinter', fingerprinter), 'from_settings': classmethod(lambda cls, settings, fingerprinter=None: cls(job_dir=settings.get('JOBDIR', '/mock/job/dir'), debug=settings.getbool('DUPEFILTER_DEBUG', False), fingerprinter=fingerprinter))}) # pragma: no cover
fingerprinter = 'mock_fingerprinter' # pragma: no cover
warn = warnings.warn # pragma: no cover

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
