# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2502833/store-output-of-subprocess-popen-call-in-a-string
from l3.Runtime import _l_
try:
    import subprocess
    _l_(896)

except ImportError:
    pass

p = subprocess.run(["echo", "hello world!"], capture_output=True, text=True)
_l_(897)
assert p.stdout == 'hello world!\n'
_l_(898)

