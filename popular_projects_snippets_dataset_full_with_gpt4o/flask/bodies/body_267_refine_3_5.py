args = [] # pragma: no cover
self = type('MockSelf', (object,), {'no_args_is_help': True})() # pragma: no cover
_env_file_option = type('MockEnvOption', (object,), {'handle_parse_result': lambda ctx, a, b: None})() # pragma: no cover
ctx = type('MockCtx', (object,), {})() # pragma: no cover
_app_option = type('MockAppOption', (object,), {'handle_parse_result': lambda ctx, a, b: None})() # pragma: no cover

import argparse # pragma: no cover
from unittest.mock import Mock # pragma: no cover

args = [] # pragma: no cover
self = Mock() # pragma: no cover
self.no_args_is_help = True # pragma: no cover
_env_file_option = Mock() # pragma: no cover
_env_file_option.handle_parse_result = Mock() # pragma: no cover
_env_file_option.handle_parse_result.side_effect = lambda ctx, opts, args: None # pragma: no cover
ctx = Mock() # pragma: no cover
_app_option = Mock() # pragma: no cover
_app_option.handle_parse_result = Mock() # pragma: no cover
_app_option.handle_parse_result.side_effect = lambda ctx, opts, args: None # pragma: no cover
def parse_args_mock(ctx, args): return [] # pragma: no cover
type(self).parse_args = Mock(side_effect=parse_args_mock) # pragma: no cover

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
