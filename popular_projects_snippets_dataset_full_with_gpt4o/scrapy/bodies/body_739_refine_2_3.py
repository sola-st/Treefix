from scrapy.commands import ScrapyCommand # pragma: no cover
from scrapy.exceptions import UsageError # pragma: no cover

class MockSettings: # pragma: no cover
    def set(self, key, value, priority): # pragma: no cover
        pass # pragma: no cover
class MockOptions: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.spargs = [] # pragma: no cover
        self.output = None # pragma: no cover
        self.overwrite_output = None # pragma: no cover
        self.output_format = None # pragma: no cover
def arglist_to_dict(arglist): # pragma: no cover
    if not isinstance(arglist, list): # pragma: no cover
        raise ValueError('arglist should be a list') # pragma: no cover
    return {arg.split('=')[0]: arg.split('=')[1] for arg in arglist if '=' in arg} # pragma: no cover
def feed_process_params_from_cli(settings, output, output_format, overwrite_output): # pragma: no cover
    return {'output': output, 'format': output_format, 'overwrite': overwrite_output} # pragma: no cover
self = type('MockSelf', (object,), {'settings': MockSettings()})() # pragma: no cover
args = [] # pragma: no cover
opts = MockOptions() # pragma: no cover

from scrapy.commands import ScrapyCommand # pragma: no cover
from scrapy.exceptions import UsageError # pragma: no cover

class MockSettings: # pragma: no cover
    def set(self, key, value, priority): # pragma: no cover
        pass # pragma: no cover
class MockOptions: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.spargs = [] # pragma: no cover
        self.output = None # pragma: no cover
        self.overwrite_output = None # pragma: no cover
        self.output_format = None # pragma: no cover
def arglist_to_dict(arglist): # pragma: no cover
    if not isinstance(arglist, list): # pragma: no cover
        raise ValueError('arglist should be a list') # pragma: no cover
    return {arg.split('=')[0]: arg.split('=')[1] for arg in arglist if '=' in arg} # pragma: no cover
def feed_process_params_from_cli(settings, output, output_format, overwrite_output): # pragma: no cover
    return {'output': output, 'format': output_format, 'overwrite': overwrite_output} # pragma: no cover
self = type('MockSelf', (object,), {'settings': MockSettings()})() # pragma: no cover
args = [] # pragma: no cover
opts = MockOptions() # pragma: no cover
ScrapyCommand.process_options = lambda self, args, opts: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/commands/__init__.py
from l3.Runtime import _l_
ScrapyCommand.process_options(self, args, opts)
_l_(17589)
try:
    _l_(17593)

    opts.spargs = arglist_to_dict(opts.spargs)
    _l_(17590)
except ValueError:
    _l_(17592)

    raise UsageError("Invalid -a value, use -a NAME=VALUE", print_help=False)
    _l_(17591)
if opts.output or opts.overwrite_output:
    _l_(17596)

    feeds = feed_process_params_from_cli(
        self.settings,
        opts.output,
        opts.output_format,
        opts.overwrite_output,
    )
    _l_(17594)
    self.settings.set('FEEDS', feeds, priority='cmdline')
    _l_(17595)
