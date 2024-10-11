store_uri = 's3://example-bucket/' # pragma: no cover
NotConfigured = Exception('Configuration not set') # pragma: no cover
settings = {'FILES_EXPIRES': 3600, 'FILES_URLS_FIELD': 'file_urls', 'FILES_RESULT_FIELD': 'file_results'} # pragma: no cover

store_uri = 's3://example-bucket/path/' # pragma: no cover
NotConfigured = Exception('Configuration not set') # pragma: no cover
settings = {'FILES_EXPIRES': 3600, 'FILES_URLS_FIELD': 'file_urls', 'FILES_RESULT_FIELD': 'file_results'} # pragma: no cover
class Settings:# pragma: no cover
    def __init__(self, settings=None):# pragma: no cover
        self.settings = settings or {}# pragma: no cover
    def getint(self, key, default):# pragma: no cover
        return int(self.settings.get(key, default))# pragma: no cover
    def get(self, key, default):# pragma: no cover
        return self.settings.get(key, default) # pragma: no cover
download_func = lambda x: f'Downloaded {x}' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/pipelines/files.py
from l3.Runtime import _l_
if not store_uri:
    _l_(9193)

    raise NotConfigured
    _l_(9192)

if isinstance(settings, dict) or settings is None:
    _l_(9195)

    settings = Settings(settings)
    _l_(9194)

cls_name = "FilesPipeline"
_l_(9196)
self.store = self._get_store(store_uri)
_l_(9197)
resolve = functools.partial(self._key_for_pipe,
                            base_class_name=cls_name,
                            settings=settings)
_l_(9198)
self.expires = settings.getint(
    resolve('FILES_EXPIRES'), self.EXPIRES
)
_l_(9199)
if not hasattr(self, "FILES_URLS_FIELD"):
    _l_(9201)

    self.FILES_URLS_FIELD = self.DEFAULT_FILES_URLS_FIELD
    _l_(9200)
if not hasattr(self, "FILES_RESULT_FIELD"):
    _l_(9203)

    self.FILES_RESULT_FIELD = self.DEFAULT_FILES_RESULT_FIELD
    _l_(9202)
self.files_urls_field = settings.get(
    resolve('FILES_URLS_FIELD'), self.FILES_URLS_FIELD
)
_l_(9204)
self.files_result_field = settings.get(
    resolve('FILES_RESULT_FIELD'), self.FILES_RESULT_FIELD
)
_l_(9205)

super().__init__(download_func=download_func, settings=settings)
_l_(9206)
