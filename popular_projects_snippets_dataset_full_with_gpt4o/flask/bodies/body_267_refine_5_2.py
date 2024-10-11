from types import SimpleNamespace # pragma: no cover

args = [] # pragma: no cover
self = SimpleNamespace(no_args_is_help=True) # pragma: no cover
_env_file_option = type('Mock', (object,), {'handle_parse_result': lambda self, ctx, opt, args: None})() # pragma: no cover
ctx = {} # pragma: no cover
_app_option = type('Mock', (object,), {'handle_parse_result': lambda self, ctx, opt, args: None})() # pragma: no cover

from argparse import ArgumentParser # pragma: no cover

args = [] # pragma: no cover
self = type('MockSelf', (ArgumentParser,), {'no_args_is_help': True})() # pragma: no cover
_env_file_option = type('MockEnvOption', (object,), {'handle_parse_result': lambda self, ctx, opt, args: None})() # pragma: no cover
ctx = {} # pragma: no cover
_app_option = type('MockAppOption', (object,), {'handle_parse_result': lambda self, ctx, opt, args: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
if not args and self.no_args_is_help:
    _l_(22608)

    # Attempt to load --env-file and --app early in case they
    # were given as env vars. Otherwise no_args_is_help will not
    # see commands from app.cli.
    _env_file_option.handle_parse_result(ctx, {}, [])
    _l_(22606)
    _app_option.handle_parse_result(ctx, {}, [])
    _l_(22607)
aux = super().parse_args(ctx, args)
_l_(22609)

exit(aux)
