from click.testing import CliRunner # pragma: no cover
from flask.cli import ScriptInfo # pragma: no cover
from flask import Flask # pragma: no cover

cli = None # pragma: no cover
args = ['command', '--option'] # pragma: no cover
kwargs = {} # pragma: no cover
self = type('Mock', (object,), {'app': Flask(__name__)})() # pragma: no cover

from click.testing import CliRunner # pragma: no cover
from flask.cli import ScriptInfo # pragma: no cover
from flask import Flask, cli # pragma: no cover

class MockSuper(CliRunner): # pragma: no cover
    def invoke(self, cli, args=None, **kwargs): # pragma: no cover
        return super().invoke(cli, args, **kwargs) # pragma: no cover
cli = None # pragma: no cover
args = ['command', '--option'] # pragma: no cover
kwargs = {} # pragma: no cover
self = type('Mock', (MockSuper,), {'app': Flask(__name__)})() # pragma: no cover

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
