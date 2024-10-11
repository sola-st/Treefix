from flask import Flask # pragma: no cover

app = Flask(__name__) # pragma: no cover
@app.route('/') # pragma: no cover
def index(): # pragma: no cover
    return 'Hello, World!' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Register a rule for routing incoming requests and building
        URLs. The :meth:`route` decorator is a shortcut to call this
        with the ``view_func`` argument. These are equivalent:

        .. code-block:: python

            @app.route("/")
            def index():
                ...

        .. code-block:: python

            def index():
                ...

            app.add_url_rule("/", view_func=index)

        See :ref:`url-route-registrations`.

        The endpoint name for the route defaults to the name of the view
        function if the ``endpoint`` parameter isn't passed. An error
        will be raised if a function has already been registered for the
        endpoint.

        The ``methods`` parameter defaults to ``["GET"]``. ``HEAD`` is
        always added automatically, and ``OPTIONS`` is added
        automatically by default.

        ``view_func`` does not necessarily need to be passed, but if the
        rule should participate in routing an endpoint name must be
        associated with a view function at some point with the
        :meth:`endpoint` decorator.

        .. code-block:: python

            app.add_url_rule("/", endpoint="index")

            @app.endpoint("index")
            def index():
                ...

        If ``view_func`` has a ``required_methods`` attribute, those
        methods are added to the passed and automatic methods. If it
        has a ``provide_automatic_methods`` attribute, it is used as the
        default if the parameter is not passed.

        :param rule: The URL rule string.
        :param endpoint: The endpoint name to associate with the rule
            and view function. Used when routing and building URLs.
            Defaults to ``view_func.__name__``.
        :param view_func: The view function to associate with the
            endpoint name.
        :param provide_automatic_options: Add the ``OPTIONS`` method and
            respond to ``OPTIONS`` requests automatically.
        :param options: Extra options passed to the
            :class:`~werkzeug.routing.Rule` object.
        """
raise NotImplementedError
_l_(18654)
