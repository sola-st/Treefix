# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2186525/how-to-use-glob-to-find-files-recursively
from l3.Runtime import _l_
try:
    from pathlib import Path
    _l_(12715)

except ImportError:
    pass

for path in Path('src').rglob('*.c'):
    _l_(12717)

    print(path.name)
    _l_(12716)
try:
    import fnmatch
    _l_(12719)

except ImportError:
    pass
try:
    import os
    _l_(12721)

except ImportError:
    pass

matches = []
_l_(12722)
for root, dirnames, filenames in os.walk('src'):
    _l_(12725)

    for filename in fnmatch.filter(filenames, '*.c'):
        _l_(12724)

        matches.append(os.path.join(root, filename))
        _l_(12723)

