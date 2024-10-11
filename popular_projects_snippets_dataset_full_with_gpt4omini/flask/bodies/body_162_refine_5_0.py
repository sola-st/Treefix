import os # pragma: no cover

variable_name = 'YOURAPPLICATION_SETTINGS' # pragma: no cover
silent = False # pragma: no cover
self = type('Mock', (object,), {'from_pyfile': lambda self, rv, silent: True})() # pragma: no cover

import os # pragma: no cover

os.environ['YOURAPPLICATION_SETTINGS'] = '/path/to/config/file' # pragma: no cover
variable_name = 'YOURAPPLICATION_SETTINGS' # pragma: no cover
silent = False # pragma: no cover
self = type('Mock', (object,), {'from_pyfile': lambda self, path, silent: True})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/config.py
from l3.Runtime import _l_
"""Loads a configuration from an environment variable pointing to
        a configuration file.  This is basically just a shortcut with nicer
        error messages for this line of code::

            app.config.from_pyfile(os.environ['YOURAPPLICATION_SETTINGS'])

        :param variable_name: name of the environment variable
        :param silent: set to ``True`` if you want silent failure for missing
                       files.
        :return: ``True`` if the file was loaded successfully.
        """
rv = os.environ.get(variable_name)
_l_(4930)
if not rv:
    _l_(4934)

    if silent:
        _l_(4932)

        aux = False
        _l_(4931)
        exit(aux)
    raise RuntimeError(
        f"The environment variable {variable_name!r} is not set"
        " and as such configuration could not be loaded. Set"
        " this variable and make it point to a configuration"
        " file"
    )
    _l_(4933)
aux = self.from_pyfile(rv, silent=silent)
_l_(4935)
exit(aux)
