import functools # pragma: no cover
from typing import Optional, Dict # pragma: no cover

store_uri = 's3://example-bucket/' # pragma: no cover
NotConfigured = Exception('NotConfigured') # pragma: no cover
settings = {'FILES_EXPIRES': 90, 'FILES_URLS_FIELD': 'file_urls', 'FILES_RESULT_FIELD': 'result'} # pragma: no cover
Settings = lambda x: x # pragma: no cover
self = type('MockSelf', (object,), {'_get_store': lambda s,uri: f'Store initialized with {uri}', '_key_for_pipe': lambda s, base_class_name, settings, key: key, 'EXPIRES': 30, 'DEFAULT_FILES_URLS_FIELD': 'urls', 'DEFAULT_FILES_RESULT_FIELD': 'files'})() # pragma: no cover
functools = functools # pragma: no cover
download_func = lambda: 'download function' # pragma: no cover

import functools # pragma: no cover

store_uri = 's3://example-bucket/' # pragma: no cover
class NotConfigured(Exception): pass # pragma: no cover
class Settings:# pragma: no cover
    def __init__(self, settings):# pragma: no cover
        self.settings = settings# pragma: no cover
    def getint(self, key, default):# pragma: no cover
        return int(self.settings.get(key, default))# pragma: no cover
    def get(self, key, default):# pragma: no cover
        return self.settings.get(key, default) # pragma: no cover
settings = Settings({'FILES_EXPIRES': 30, 'FILES_URLS_FIELD': 'file_urls', 'FILES_RESULT_FIELD': 'files'}) # pragma: no cover
self = type('MockSelf', (object,), {'_get_store': lambda self, uri: f'Store initialized with {uri}', '_key_for_pipe': lambda self, base_class_name, settings, key: key, 'EXPIRES': 30, 'DEFAULT_FILES_URLS_FIELD': 'urls', 'DEFAULT_FILES_RESULT_FIELD': 'files'})() # pragma: no cover
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
