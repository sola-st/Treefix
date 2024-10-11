from flask import Flask # pragma: no cover
from flask.cli import ScriptInfo # pragma: no cover
import click # pragma: no cover
from click.testing import CliRunner # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.cli = click.Group() # pragma: no cover
self = type('MockSelf', (object,), {'app': app, 'invoke': lambda cli, args, **kwargs: click.testing.Result(click.Context(cli), 0, b'Executed', b'', ())})() # pragma: no cover
cli = None # pragma: no cover
args = ['mock-command'] # pragma: no cover
kwargs = {} # pragma: no cover
class MockSuperInvoker: # pragma: no cover
    def invoke(self, cli, args, **kwargs): # pragma: no cover
        return click.testing.Result(click.Context(cli), 0, b'Executed', b'', ()) # pragma: no cover
super = MockSuperInvoker() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/testing.py
from l3.Runtime import _l_
"""Invokes a CLI command in an isolated environment. See
        :meth:`CliRunner.invoke <click.testing.CliRunner.invoke>` for
        full method documentation. See :ref:`testing-cli` for examples.

        If the ``obj`` argument is not given, passes an instance of
        :class:`~flask.cli.ScriptInfo` that knows how to load the Flask
        app being tested.

        :param cli: Command object to invoke. Default is the app's
            :attr:`~flask.app.Flask.cli` group.
        :param args: List of strings to invoke the command with.

        :return: a :class:`~click.testing.Result` object.
        """
if cli is None:
    _l_(22942)

    cli = self.app.cli  # type: ignore
    _l_(22941)  # type: ignore

if "obj" not in kwargs:
    _l_(22944)

    kwargs["obj"] = ScriptInfo(create_app=lambda: self.app)
    _l_(22943)
aux = super().invoke(cli, args, **kwargs)
_l_(22945)

exit(aux)
