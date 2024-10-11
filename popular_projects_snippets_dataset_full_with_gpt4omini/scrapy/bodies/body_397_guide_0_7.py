from importlib import import_module # pragma: no cover
import types # pragma: no cover

self = type('Mock', (object,), {'_assert_mutability': lambda self: None, 'set': lambda self, key, value, priority: None})() # pragma: no cover
module = types.ModuleType('mock_module') # pragma: no cover
setattr(module, 'TEST_VAR', 'value') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/settings/__init__.py
from l3.Runtime import _l_
"""
        Store settings from a module with a given priority.

        This is a helper function that calls
        :meth:`~scrapy.settings.BaseSettings.set` for every globally declared
        uppercase variable of ``module`` with the provided ``priority``.

        :param module: the module or the path of the module
        :type module: types.ModuleType or str

        :param priority: the priority of the settings. Should be a key of
            :attr:`~scrapy.settings.SETTINGS_PRIORITIES` or an integer
        :type priority: str or int
        """
self._assert_mutability()
_l_(10193)
if isinstance(module, str):
    _l_(10195)

    module = import_module(module)
    _l_(10194)
for key in dir(module):
    _l_(10198)

    if key.isupper():
        _l_(10197)

        self.set(key, getattr(module, key), priority)
        _l_(10196)
