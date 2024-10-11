import functools # pragma: no cover
from typing import Any, Dict, Optional # pragma: no cover

store_uri = 's3://my-bucket/my-path/' # pragma: no cover
class NotConfigured(Exception): pass # pragma: no cover
settings = {'FILES_EXPIRES': 90, 'FILES_URLS_FIELD': 'file_urls', 'FILES_RESULT_FIELD': 'file_results'} # pragma: no cover
class Settings:# pragma: no cover
    def __init__(self, settings: Optional[Dict[str, Any]]) -> None:# pragma: no cover
        self.settings = settings or {}# pragma: no cover
    # pragma: no cover
    def getint(self, key: str, default: int) -> int:# pragma: no cover
        return int(self.settings.get(key, default))# pragma: no cover
    # pragma: no cover
    def get(self, key: str, default: Any) -> Any:# pragma: no cover
        return self.settings.get(key, default) # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
def _get_store(store_uri: str) -> str:# pragma: no cover
    return f'Store connected at {store_uri}'# pragma: no cover
self._get_store = _get_store # pragma: no cover
self.EXPIRES = 30 # pragma: no cover
self.DEFAULT_FILES_URLS_FIELD = 'default_file_urls_field' # pragma: no cover
self.DEFAULT_FILES_RESULT_FIELD = 'default_file_result_field' # pragma: no cover
download_func = lambda x: x # pragma: no cover
def _key_for_pipe(key: str, base_class_name: str, settings: Any) -> str:# pragma: no cover
    return f'{base_class_name}_{key}'# pragma: no cover
self._key_for_pipe = _key_for_pipe # pragma: no cover
self.store_uri = store_uri # pragma: no cover
self.settings = Settings(settings) # pragma: no cover
self.functools = functools # pragma: no cover
self.FILES_URLS_FIELD = 'default_file_urls_field' # pragma: no cover
self.FILES_RESULT_FIELD = 'default_file_result_field' # pragma: no cover
self.files_urls_field = 'default_file_urls_field' # pragma: no cover
self.files_result_field = 'default_file_result_field' # pragma: no cover

import functools # pragma: no cover
from typing import Any, Dict, Optional # pragma: no cover

store_uri = 's3://example-bucket/' # pragma: no cover
class NotConfigured(Exception): pass # pragma: no cover
settings = {'FILES_EXPIRES': 90, 'FILES_URLS_FIELD': 'file_urls', 'FILES_RESULT_FIELD': 'files'} # pragma: no cover
class Settings:# pragma: no cover
    def __init__(self, settings: Optional[Dict[str, Any]] = None) -> None:# pragma: no cover
        self.settings = settings or {}# pragma: no cover
    def getint(self, key: str, default: int = 0) -> int:# pragma: no cover
        return int(self.settings.get(key, default))# pragma: no cover
    def get(self, key: str, default: Any = None) -> Any:# pragma: no cover
        return self.settings.get(key, default) # pragma: no cover
class BaseClass:# pragma: no cover
    def __init__(self, download_func: Optional[callable] = None, settings: Any = None) -> None:# pragma: no cover
        self.download_func = download_func# pragma: no cover
        self.settings = settings # pragma: no cover
class MockPipeline(BaseClass):# pragma: no cover
    EXPIRES = 90# pragma: no cover
    DEFAULT_FILES_URLS_FIELD = 'file_urls'# pragma: no cover
    DEFAULT_FILES_RESULT_FIELD = 'files'# pragma: no cover
    def _get_store(self, uri: str) -> str:# pragma: no cover
        return 'mock_store'# pragma: no cover
    def _key_for_pipe(self, key: str, base_class_name: str, settings: Dict[str, Any]) -> str:# pragma: no cover
        return f'{base_class_name}_{key}' # pragma: no cover
self = MockPipeline() # pragma: no cover
download_func = lambda url: f'downloading {url}' # pragma: no cover

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
