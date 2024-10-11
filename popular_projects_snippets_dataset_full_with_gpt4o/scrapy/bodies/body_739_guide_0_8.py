from scrapy.exceptions import UsageError # pragma: no cover

class MockSettings: pass # pragma: no cover
class MockOpts: spargs = 'invalid_format' ; output = None; overwrite_output = None # pragma: no cover
class MockSelf: settings = MockSettings() # pragma: no cover
def arglist_to_dict(arglist): raise ValueError # pragma: no cover
def feed_process_params_from_cli(settings, output, output_format, overwrite_output): return {} # pragma: no cover
self = MockSelf() # pragma: no cover
args, opts = [], MockOpts() # pragma: no cover

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
