# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python
#!/usr/bin/env python
from l3.Runtime import _l_
try:
    import signal
    _l_(3440)

except ImportError:
    pass
try:
    import sys
    _l_(3442)

except ImportError:
    pass

def signal_handler(sig, frame):
    _l_(3445)

    print('You pressed Ctrl+C!')
    _l_(3443)
    sys.exit(0)
    _l_(3444)

signal.signal(signal.SIGINT, signal_handler)
_l_(3446)
print('Press Ctrl+C')
_l_(3447)
signal.pause()
_l_(3448)

