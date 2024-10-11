import sys # pragma: no cover
import glob # pragma: no cover
import os # pragma: no cover

test_dir = tempfile.mkdtemp() # pragma: no cover
test_file_path = os.path.join(test_dir, 'test_script.py') # pragma: no cover
with open(test_file_path, 'w') as f: f.write('print("Hello, World!")') # pragma: no cover
sys.argv = ['script_name.py', test_dir] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4284313/how-can-i-check-the-syntax-of-python-script-without-executing-it
from l3.Runtime import _l_
try:
    import sys
    _l_(14206)

except ImportError:
    pass
try:
    import glob, os
    _l_(14208)

except ImportError:
    pass

os.chdir(sys.argv[1])
_l_(14209)
for file in glob.glob("*.py"):
    _l_(14212)

    source = open(file, 'r').read() + '\n'
    _l_(14210)
    compile(source, file, 'exec')
    _l_(14211)

