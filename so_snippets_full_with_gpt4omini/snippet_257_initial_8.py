from signal import pthread_kill, SIGTSTP # pragma: no cover
from threading import Thread # pragma: no cover
from itertools import count # pragma: no cover
from time import sleep # pragma: no cover

Stopped = 'Stopped' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread
from l3.Runtime import _l_
try:
    from signal import pthread_kill, SIGTSTP
    _l_(1713)

except ImportError:
    pass
try:
    from threading import Thread
    _l_(1715)

except ImportError:
    pass
try:
    from itertools import count
    _l_(1717)

except ImportError:
    pass
try:
    from time import sleep
    _l_(1719)

except ImportError:
    pass

def target():
    _l_(1723)

    for num in count():
        _l_(1722)

        print(num)
        _l_(1720)
        sleep(1)
        _l_(1721)

thread = Thread(target=target)
_l_(1724)
thread.start()
_l_(1725)
sleep(5)
_l_(1726)
pthread_kill(thread.ident, SIGTSTP)
_l_(1727)

0
_l_(1728)
1
_l_(1729)
2
_l_(1730)
3
_l_(1731)
4
_l_(1732)

[14]+  Stopped
_l_(1733)

