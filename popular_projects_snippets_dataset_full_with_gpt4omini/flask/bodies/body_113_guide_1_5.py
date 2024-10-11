from flask import Flask # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

self = type('Mock', (object,), {'test_cli_runner_class': None})() # pragma: no cover
cls = None # pragma: no cover
kwargs = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Create a CLI runner for testing CLI commands.
        See :ref:`testing-cli`.

        Returns an instance of :attr:`test_cli_runner_class`, by default
        :class:`~flask.testing.FlaskCliRunner`. The Flask app object is
        passed as the first argument.

        .. versionadded:: 1.0
        """
cls = self.test_cli_runner_class
_l_(8782)

if cls is None:
    _l_(8785)

    try:
        from .testing import FlaskCliRunner as cls
        _l_(8784)

    except ImportError:
        pass
aux = cls(self, **kwargs)  # type: ignore
_l_(8786)  # type: ignore

exit(aux)  # type: ignore
