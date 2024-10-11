import signal # pragma: no cover
from unittest.mock import Mock # pragma: no cover

pthread_kill = Mock(side_effect=ImportError) # pragma: no cover
SIGTSTP = Mock(side_effect=ImportError) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread
from l3.Runtime import _l_
try:
    from signal import pthread_kill, SIGTSTP
    _l_(13539)

except ImportError:
    pass
try:
    from threading import Thread
    _l_(13541)

except ImportError:
    pass
try:
    from itertools import count
    _l_(13543)

except ImportError:
    pass
try:
    from time import sleep
    _l_(13545)

except ImportError:
    pass

def target():
    _l_(13549)

    for num in count():
        _l_(13548)

        print(num)
        _l_(13546)
        sleep(1)
        _l_(13547)

thread = Thread(target=target)
_l_(13550)
thread.start()
_l_(13551)
sleep(5)
_l_(13552)
pthread_kill(thread.ident, SIGTSTP)
_l_(13553)

0
_l_(13554)
1
_l_(13555)
2
_l_(13556)
3
_l_(13557)
4
_l_(13558)

[14]+  Stopped
_l_(13559)

