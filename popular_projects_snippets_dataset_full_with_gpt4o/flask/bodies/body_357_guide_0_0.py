from flask import Flask # pragma: no cover
from flask.cli import ScriptInfo # pragma: no cover
import click.testing # pragma: no cover

class MockApp: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.cli = click.Group() # pragma: no cover
 # pragma: no cover
mock_app = MockApp() # pragma: no cover
self = type('MockSelf', (object,), {'app': mock_app, 'invoke': click.testing.CliRunner().invoke})() # pragma: no cover
cli = None # pragma: no cover
args = [] # pragma: no cover
kwargs = {} # pragma: no cover
aux = None # pragma: no cover
 # pragma: no cover
# Assuming there's a CLI command to test/execute # pragma: no cover
mock_command = click.Command('mock', callback=lambda: None) # pragma: no cover
self.app.cli.add_command(mock_command) # pragma: no cover

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
