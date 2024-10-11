bytes # pragma: no cover

lines = [b'example line with substring', b'another line', b'substring present here'] # pragma: no cover

from typing import List # pragma: no cover

lines: List[bytes] = [b'first line with substring', b'second line', b'third line with substring'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/33054527/typeerror-a-bytes-like-object-is-required-not-str-when-writing-to-a-file-in
from l3.Runtime import _l_
for line in lines:
    _l_(1104)

    print(type(line))# <class 'bytes'>
    _l_(1101)# <class 'bytes'>
    if 'substring' in line:
        _l_(1103)

        print('success')
        _l_(1102)

for line in lines:
    _l_(1109)

    line = line.decode()
    _l_(1105)
    print(type(line))# <class 'str'>
    _l_(1106)# <class 'str'>
    if 'substring' in line:
        _l_(1108)

        print('success')
        _l_(1107)

