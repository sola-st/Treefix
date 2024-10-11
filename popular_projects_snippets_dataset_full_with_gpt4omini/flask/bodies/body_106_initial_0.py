# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Returns the shell context for an interactive shell for this
        application.  This runs all the registered shell context
        processors.

        .. versionadded:: 0.11
        """
rv = {"app": self, "g": g}
_l_(6891)
for processor in self.shell_context_processors:
    _l_(6893)

    rv.update(processor())
    _l_(6892)
aux = rv
_l_(6894)
exit(aux)
