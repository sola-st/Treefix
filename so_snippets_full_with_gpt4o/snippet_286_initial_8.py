lines = [b'This is a test substring in bytes.', b'Another line without the keyword.'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/33054527/typeerror-a-bytes-like-object-is-required-not-str-when-writing-to-a-file-in
from l3.Runtime import _l_
for line in lines:
    _l_(12714)

    print(type(line))# <class 'bytes'>
    _l_(12711)# <class 'bytes'>
    if 'substring' in line:
        _l_(12713)

        print('success')
        _l_(12712)

for line in lines:
    _l_(12719)

    line = line.decode()
    _l_(12715)
    print(type(line))# <class 'str'>
    _l_(12716)# <class 'str'>
    if 'substring' in line:
        _l_(12718)

        print('success')
        _l_(12717)

