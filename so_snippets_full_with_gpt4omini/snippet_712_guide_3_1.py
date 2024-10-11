import sys # pragma: no cover
import glob # pragma: no cover
import os # pragma: no cover

sys.argv = ['script.py', 'test_directory'] # pragma: no cover
os.makedirs('test_directory', exist_ok=True) # pragma: no cover
with open('test_directory/example.py', 'w') as f: f.write('print(\"Hello, World!\")') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4284313/how-can-i-check-the-syntax-of-python-script-without-executing-it
from l3.Runtime import _l_
try:
    import sys
    _l_(1767)

except ImportError:
    pass
try:
    import glob, os
    _l_(1769)

except ImportError:
    pass

os.chdir(sys.argv[1])
_l_(1770)
for file in glob.glob("*.py"):
    _l_(1773)

    source = open(file, 'r').read() + '\n'
    _l_(1771)
    compile(source, file, 'exec')
    _l_(1772)

