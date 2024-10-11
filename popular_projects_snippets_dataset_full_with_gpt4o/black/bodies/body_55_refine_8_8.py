self = type('Mock', (object,), {'failure_count': 0, 'change_count': 1, 'check': True})() # pragma: no cover

import sys # pragma: no cover

class MockApp: # pragma: no cover
    def __init__(self, failure_count, change_count, check): # pragma: no cover
        self.failure_count = failure_count # pragma: no cover
        self.change_count = change_count # pragma: no cover
        self.check = check # pragma: no cover
 # pragma: no cover
 # pragma: no cover
self = MockApp(failure_count=0, change_count=1, check=True) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/report.py
from l3.Runtime import _l_
"""Return the exit code that the app should use.

        This considers the current state of changed files and failures:
        - if there were any failures, return 123;
        - if any files were changed and --check is being used, return 1;
        - otherwise return 0.
        """
# According to http://tldp.org/LDP/abs/html/exitcodes.html starting with
# 126 we have special return codes reserved by the shell.
if self.failure_count:
    _l_(19306)

    aux = 123
    _l_(19303)
    exit(aux)

elif self.change_count and self.check:
    _l_(19305)

    aux = 1
    _l_(19304)
    exit(aux)
aux = 0
_l_(19307)

exit(aux)
