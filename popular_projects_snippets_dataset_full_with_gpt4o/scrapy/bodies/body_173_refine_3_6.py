import functools # pragma: no cover

store_uri = 'some_store_uri' # pragma: no cover
settings = {'FILES_EXPIRES': 90, 'FILES_URLS_FIELD': 'urls', 'FILES_RESULT_FIELD': 'results'} # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self._get_store = lambda uri: 'store_mock' # pragma: no cover
self._key_for_pipe = lambda base_class_name, settings, key: key.upper() # pragma: no cover
self.EXPIRES = 30 # pragma: no cover
self.DEFAULT_FILES_URLS_FIELD = 'default_urls_field' # pragma: no cover
self.DEFAULT_FILES_RESULT_FIELD = 'default_results_field' # pragma: no cover
download_func = lambda uri: 'download_mock' # pragma: no cover

import functools # pragma: no cover

store_uri = 'some_store_uri' # pragma: no cover
class NotConfigured(Exception): pass # pragma: no cover
class Settings: # pragma: no cover
    def __init__(self, settings): # pragma: no cover
        if isinstance(settings, dict) or settings is None: # pragma: no cover
            self._settings = settings or {} # pragma: no cover
        else: # pragma: no cover
            raise ValueError('Expected a dictionary or None') # pragma: no cover
    def get(self, key, default=None): # pragma: no cover
        return self._settings.get(key, default) # pragma: no cover
    def getint(self, key, default=0): # pragma: no cover
        return int(self._settings.get(key, default)) # pragma: no cover
settings_dict = {'FILES_EXPIRES': 90, 'FILES_URLS_FIELD': 'urls', 'FILES_RESULT_FIELD': 'results'} # pragma: no cover
settings = Settings(settings_dict) # pragma: no cover
self = type('Mock', (object,), {'_get_store': lambda uri: 'store_mock', '_key_for_pipe': lambda base_class_name, settings, key: key.upper()})() # pragma: no cover
self.EXPIRES = 30 # pragma: no cover
self.DEFAULT_FILES_URLS_FIELD = 'default_urls_field' # pragma: no cover
self.DEFAULT_FILES_RESULT_FIELD = 'default_results_field' # pragma: no cover
download_func = lambda uri: 'download_mock' # pragma: no cover

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
