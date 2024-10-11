import functools # pragma: no cover
from scrapy.exceptions import NotConfigured # pragma: no cover
from scrapy.settings import Settings # pragma: no cover

store_uri = 'http://example.com/storage' # pragma: no cover
settings = Settings() # pragma: no cover
class MockBase:# pragma: no cover
  EXPIRES = 90# pragma: no cover
  DEFAULT_FILES_URLS_FIELD = 'file_urls'# pragma: no cover
  DEFAULT_FILES_RESULT_FIELD = 'files'# pragma: no cover
  def _get_store(self, uri):# pragma: no cover
    return 'mock_store'# pragma: no cover
  def _key_for_pipe(self, key, base_class_name, settings):# pragma: no cover
    return key# pragma: no cover
MockSelf = type('MockSelf', (MockBase,), {}) # pragma: no cover
self = MockSelf() # pragma: no cover
download_func = lambda: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
from l3.Runtime import _l_
if not store_uri:
    _l_(20692)

    raise NotConfigured
    _l_(20691)

if isinstance(settings, dict) or settings is None:
    _l_(20694)

    settings = Settings(settings)
    _l_(20693)

cls_name = "FilesPipeline"
_l_(20695)
self.store = self._get_store(store_uri)
_l_(20696)
resolve = functools.partial(self._key_for_pipe,
                            base_class_name=cls_name,
                            settings=settings)
_l_(20697)
self.expires = settings.getint(
    resolve('FILES_EXPIRES'), self.EXPIRES
)
_l_(20698)
if not hasattr(self, "FILES_URLS_FIELD"):
    _l_(20700)

    self.FILES_URLS_FIELD = self.DEFAULT_FILES_URLS_FIELD
    _l_(20699)
if not hasattr(self, "FILES_RESULT_FIELD"):
    _l_(20702)

    self.FILES_RESULT_FIELD = self.DEFAULT_FILES_RESULT_FIELD
    _l_(20701)
self.files_urls_field = settings.get(
    resolve('FILES_URLS_FIELD'), self.FILES_URLS_FIELD
)
_l_(20703)
self.files_result_field = settings.get(
    resolve('FILES_RESULT_FIELD'), self.FILES_RESULT_FIELD
)
_l_(20704)

super().__init__(download_func=download_func, settings=settings)
_l_(20705)
