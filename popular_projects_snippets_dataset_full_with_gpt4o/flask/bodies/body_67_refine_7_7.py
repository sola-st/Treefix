from typing import Any # pragma: no cover
import flask # pragma: no cover
from flask import Flask, Response # pragma: no cover

cls = type('Mock', (object,), {'init_every_request': True, 'decorators': [], '__module__': '__main__', '__doc__': 'Mock class for testing purposes', 'methods': ['GET'], 'provide_automatic_options': True, 'dispatch_request': lambda self, **kwargs: 'response'}) # pragma: no cover
t = type('Mock', (object,), {'Any': Any}) # pragma: no cover
ft = type('Mock', (object,), {'ResponseReturnValue': Response}) # pragma: no cover
class_args = () # pragma: no cover
class_kwargs = {} # pragma: no cover
name = 'mock_view' # pragma: no cover
current_app = type('MockApp', (object,), {'ensure_sync': lambda x: x})() # pragma: no cover

from typing import Any # pragma: no cover
from flask import Flask, Response, current_app # pragma: no cover

class MockClass: # pragma: no cover
    init_every_request = True # pragma: no cover
    decorators = [] # pragma: no cover
    __module__ = '__main__' # pragma: no cover
    __doc__ = 'Mock class for testing purposes' # pragma: no cover
    methods = ['GET'] # pragma: no cover
    provide_automatic_options = True # pragma: no cover
    def dispatch_request(self, **kwargs: Any) -> Response: # pragma: no cover
        return Response('response') # pragma: no cover
 # pragma: no cover
cls = MockClass # pragma: no cover
 # pragma: no cover
t = type('MockT', (object,), {'Any': Any}) # pragma: no cover
 # pragma: no cover
class MockFT: # pragma: no cover
    ResponseReturnValue = Response # pragma: no cover
 # pragma: no cover
ft = MockFT # pragma: no cover
 # pragma: no cover
class_args = () # pragma: no cover
class_kwargs = {} # pragma: no cover
name = 'mock_view' # pragma: no cover
 # pragma: no cover
class MockCurrentApp: # pragma: no cover
    @staticmethod # pragma: no cover
    def ensure_sync(func): # pragma: no cover
        return func # pragma: no cover
 # pragma: no cover
current_app = MockCurrentApp() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/views.py
from l3.Runtime import _l_
"""Convert the class into a view function that can be registered
        for a route.

        By default, the generated view will create a new instance of the
        view class for every request and call its
        :meth:`dispatch_request` method. If the view class sets
        :attr:`init_every_request` to ``False``, the same instance will
        be used for every request.

        Except for ``name``, all other arguments passed to this method
        are forwarded to the view class ``__init__`` method.

        .. versionchanged:: 2.2
            Added the ``init_every_request`` class attribute.
        """
if cls.init_every_request:
    _l_(16345)


    def view(**kwargs: t.Any) -> ft.ResponseReturnValue:
        _l_(16341)

        self = view.view_class(  # type: ignore[attr-defined]
            *class_args, **class_kwargs
        )
        _l_(16339)
        aux = current_app.ensure_sync(self.dispatch_request)(**kwargs)
        _l_(16340)
        exit(aux)

else:
    self = cls(*class_args, **class_kwargs)
    _l_(16342)

    def view(**kwargs: t.Any) -> ft.ResponseReturnValue:
        _l_(16344)

        aux = current_app.ensure_sync(self.dispatch_request)(**kwargs)
        _l_(16343)
        exit(aux)

if cls.decorators:
    _l_(16350)

    view.__name__ = name
    _l_(16346)
    view.__module__ = cls.__module__
    _l_(16347)
    for decorator in cls.decorators:
        _l_(16349)

        view = decorator(view)
        _l_(16348)
view.view_class = cls  # type: ignore
_l_(16351)  # type: ignore
view.__name__ = name
_l_(16352)
view.__doc__ = cls.__doc__
_l_(16353)
view.__module__ = cls.__module__
_l_(16354)
view.methods = cls.methods  # type: ignore
_l_(16355)  # type: ignore
view.provide_automatic_options = cls.provide_automatic_options  # type: ignore
_l_(16356)  # type: ignore
aux = view
_l_(16357)
exit(aux)
