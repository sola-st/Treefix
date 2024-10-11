from flask import g # pragma: no cover

self = type('Mock', (object,), {'shell_context_processors': [lambda: {'key': 'value'}]})() # pragma: no cover
g = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Returns the shell context for an interactive shell for this
        application.  This runs all the registered shell context
        processors.

        .. versionadded:: 0.11
        """
rv = {"app": self, "g": g}
_l_(18188)
for processor in self.shell_context_processors:
    _l_(18190)

    rv.update(processor())
    _l_(18189)
aux = rv
_l_(18191)
exit(aux)
