# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
from l3.Runtime import _l_
try:
    import os
    _l_(1088)

except ImportError:
    pass

# Clear Windows command prompt.
if (os.name in ('ce', 'nt', 'dos')):
    _l_(1092)

    os.system('cls')
    _l_(1089)

# Clear the Linux terminal.
elif ('posix' in os.name):
    _l_(1091)

    os.system('clear')
    _l_(1090)
try:
    import os
    _l_(1094)

except ImportError:
    pass

def clear():
    _l_(1099)

    if os.name == 'posix':
        _l_(1098)

        os.system('clear')
        _l_(1095)

    elif os.name in ('ce', 'nt', 'dos'):
        _l_(1097)

        os.system('cls')
        _l_(1096)


clear()
_l_(1100)

