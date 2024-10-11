import argparse # pragma: no cover
class MockOption: pass # pragma: no cover
class MockContext: pass # pragma: no cover

args = [] # pragma: no cover
self = type('Mock', (), {'no_args_is_help': True})() # pragma: no cover
_env_file_option = MockOption() # pragma: no cover
ctx = MockContext() # pragma: no cover
_app_option = MockOption() # pragma: no cover
_env_file_option.handle_parse_result = lambda ctx, a, b: None # pragma: no cover
_app_option.handle_parse_result = lambda ctx, a, b: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
if not args and self.no_args_is_help:
    _l_(5371)

    # Attempt to load --env-file and --app early in case they
    # were given as env vars. Otherwise no_args_is_help will not
    # see commands from app.cli.
    _env_file_option.handle_parse_result(ctx, {}, [])
    _l_(5369)
    _app_option.handle_parse_result(ctx, {}, [])
    _l_(5370)
aux = super().parse_args(ctx, args)
_l_(5372)

exit(aux)
