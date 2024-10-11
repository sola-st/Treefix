class MockApp: pass # pragma: no cover
class MockAbort: pass # pragma: no cover
class MockMakeResponse: pass # pragma: no cover
class MockRedirect: pass # pragma: no cover
class MockRenderTemplate: pass # pragma: no cover
class MockRequest: pass # pragma: no cover
class MockSession: pass # pragma: no cover

app = MockApp() # pragma: no cover
abort = MockAbort() # pragma: no cover
make_response = MockMakeResponse() # pragma: no cover
redirect = MockRedirect() # pragma: no cover
render_template = MockRenderTemplate() # pragma: no cover
request = MockRequest() # pragma: no cover
session = MockSession() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/53162/how-can-i-do-a-line-break-line-continuation-in-python
from l3.Runtime import _l_
try:
    from app import (
        app, abort, make_response, redirect, render_template, request, session
    )
    _l_(11839)

except ImportError:
    pass

