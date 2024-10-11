import os # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
from l3.Runtime import _l_
try:
    import os
    _l_(13273)

except ImportError:
    pass

# Clear Windows command prompt.
if (os.name in ('ce', 'nt', 'dos')):
    _l_(13277)

    os.system('cls')
    _l_(13274)

# Clear the Linux terminal.
elif ('posix' in os.name):
    _l_(13276)

    os.system('clear')
    _l_(13275)
try:
    import os
    _l_(13279)

except ImportError:
    pass

def clear():
    _l_(13284)

    if os.name == 'posix':
        _l_(13283)

        os.system('clear')
        _l_(13280)

    elif os.name in ('ce', 'nt', 'dos'):
        _l_(13282)

        os.system('cls')
        _l_(13281)


clear()
_l_(13285)

