import sys # pragma: no cover

class MockSelf: # pragma: no cover
    debug = True # pragma: no cover
self = MockSelf() # pragma: no cover
class MockDebugHelpersModule: # pragma: no cover
    class FormDataRoutingRedirect(Exception): # pragma: no cover
        def __init__(self, request): # pragma: no cover
            self.request = request # pragma: no cover
sys.modules['.debughelpers'] = MockDebugHelpersModule # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Intercept routing exceptions and possibly do something else.

        In debug mode, intercept a routing redirect and replace it with
        an error if the body will be discarded.

        With modern Werkzeug this shouldn't occur, since it now uses a
        308 status which tells the browser to resend the method and
        body.

        .. versionchanged:: 2.1
            Don't intercept 307 and 308 redirects.

        :meta private:
        :internal:
        """
if (
    not self.debug
    or not isinstance(request.routing_exception, RequestRedirect)
    or request.routing_exception.code in {307, 308}
    or request.method in {"GET", "HEAD", "OPTIONS"}
):
    _l_(22930)

    raise request.routing_exception  # type: ignore
    _l_(22929)  # type: ignore
try:
    from .debughelpers import FormDataRoutingRedirect
    _l_(22932)

except ImportError:
    pass

raise FormDataRoutingRedirect(request)
_l_(22933)
