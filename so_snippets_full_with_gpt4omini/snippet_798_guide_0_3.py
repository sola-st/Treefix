file_path = r'C:\Users\Bob\SecretPasswordFile.txt' # pragma: no cover
mock_open = type('MockOpen', (object,), {'read': lambda self: 'mocked_password'}) # pragma: no cover
open = lambda path: mock_open() if path == file_path else __builtins__.open(path) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1347791/unicode-error-unicodeescape-codec-cant-decode-bytes-cannot-open-text-file
from l3.Runtime import _l_
passwordFile = open(r'''C:\Users\Bob\SecretPasswordFile.txt''')
_l_(2408)

