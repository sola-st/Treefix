from typing import List, Any # pragma: no cover

class MockRequest: # pragma: no cover
    pass
key = 'example' # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.msg = '' # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/debughelpers.py
from l3.Runtime import _l_
form_matches = request.form.getlist(key)
_l_(19394)
buf = [
    f"You tried to access the file {key!r} in the request.files"
    " dictionary but it does not exist. The mimetype for the"
    f" request is {request.mimetype!r} instead of"
    " 'multipart/form-data' which means that no file contents"
    " were transmitted. To fix this error you should provide"
    ' enctype="multipart/form-data" in your form.'
]
_l_(19395)
if form_matches:
    _l_(19398)

    names = ", ".join(repr(x) for x in form_matches)
    _l_(19396)
    buf.append(
        "\n\nThe browser instead transmitted some file names. "
        f"This was submitted: {names}"
    )
    _l_(19397)
self.msg = "".join(buf)
_l_(19399)
