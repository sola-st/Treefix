from collections import namedtuple # pragma: no cover
from werkzeug.datastructures import MultiDict # pragma: no cover

MockRequest = type('MockRequest', (object,), {'form': MultiDict({'file_input': ['file1.txt', 'file2.txt']}), 'mimetype': 'application/x-www-form-urlencoded'}) # pragma: no cover
request = MockRequest() # pragma: no cover
key = 'file_input' # pragma: no cover
self = type('MockSelf', (object,), {'msg': ''})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/debughelpers.py
from l3.Runtime import _l_
form_matches = request.form.getlist(key)
_l_(8257)
buf = [
    f"You tried to access the file {key!r} in the request.files"
    " dictionary but it does not exist. The mimetype for the"
    f" request is {request.mimetype!r} instead of"
    " 'multipart/form-data' which means that no file contents"
    " were transmitted. To fix this error you should provide"
    ' enctype="multipart/form-data" in your form.'
]
_l_(8258)
if form_matches:
    _l_(8261)

    names = ", ".join(repr(x) for x in form_matches)
    _l_(8259)
    buf.append(
        "\n\nThe browser instead transmitted some file names. "
        f"This was submitted: {names}"
    )
    _l_(8260)
self.msg = "".join(buf)
_l_(8262)
