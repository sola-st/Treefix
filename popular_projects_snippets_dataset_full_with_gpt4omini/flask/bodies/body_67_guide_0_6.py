from flask import Flask, Response as ft, current_app # pragma: no cover

app = Flask(__name__) # pragma: no cover
class MockClass:  # mock class to test the view function # pragma: no cover
    init_every_request = True # pragma: no cover
    methods = ['GET'] # pragma: no cover
    decorators = [] # pragma: no cover
    provide_automatic_options = True # pragma: no cover
    def dispatch_request(self): # pragma: no cover
        return 'Hello, World!' # pragma: no cover
cls = MockClass # pragma: no cover
class_args = () # pragma: no cover
class_kwargs = {} # pragma: no cover
name = 'mock_view' # pragma: no cover

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
    _l_(4640)


    def view(**kwargs: t.Any) -> ft.ResponseReturnValue:
        _l_(4636)

        self = view.view_class(  # type: ignore[attr-defined]
            *class_args, **class_kwargs
        )
        _l_(4634)
        aux = current_app.ensure_sync(self.dispatch_request)(**kwargs)
        _l_(4635)
        exit(aux)

else:
    self = cls(*class_args, **class_kwargs)
    _l_(4637)

    def view(**kwargs: t.Any) -> ft.ResponseReturnValue:
        _l_(4639)

        aux = current_app.ensure_sync(self.dispatch_request)(**kwargs)
        _l_(4638)
        exit(aux)

if cls.decorators:
    _l_(4645)

    view.__name__ = name
    _l_(4641)
    view.__module__ = cls.__module__
    _l_(4642)
    for decorator in cls.decorators:
        _l_(4644)

        view = decorator(view)
        _l_(4643)
view.view_class = cls  # type: ignore
_l_(4646)  # type: ignore
view.__name__ = name
_l_(4647)
view.__doc__ = cls.__doc__
_l_(4648)
view.__module__ = cls.__module__
_l_(4649)
view.methods = cls.methods  # type: ignore
_l_(4650)  # type: ignore
view.provide_automatic_options = cls.provide_automatic_options  # type: ignore
_l_(4651)  # type: ignore
aux = view
_l_(4652)
exit(aux)
