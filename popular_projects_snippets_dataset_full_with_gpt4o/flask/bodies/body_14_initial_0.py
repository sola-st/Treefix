from typing import List # pragma: no cover
import contextvars # pragma: no cover

# Define a self-contained mock class for app # pragma: no cover
class MockApp: # pragma: no cover
    def create_url_adapter(self, arg): # pragma: no cover
        # Mock implementation # pragma: no cover
        return 'mock_url_adapter' # pragma: no cover
    def app_ctx_globals_class(self): # pragma: no cover
        # Mock implementation # pragma: no cover
        return MockAppCtxGlobals() # pragma: no cover
 # pragma: no cover
# Define a self-contained mock class for _AppCtxGlobals # pragma: no cover
class MockAppCtxGlobals: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
# Initialize the undefined variables # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
app = MockApp() # pragma: no cover
_AppCtxGlobals = MockAppCtxGlobals # pragma: no cover
t = type('MockT', (object,), {'List': List}) # pragma: no cover
contextvars = type('MockContextVars', (object,), {'Token': contextvars.Token}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
self.app = app
_l_(18650)
self.url_adapter = app.create_url_adapter(None)
_l_(18651)
self.g: _AppCtxGlobals = app.app_ctx_globals_class()
_l_(18652)
self._cv_tokens: t.List[contextvars.Token] = []
_l_(18653)
