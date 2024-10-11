from scrapy.commands import ScrapyCommand # pragma: no cover
from scrapy.exceptions import UsageError # pragma: no cover
from scrapy.settings import Settings # pragma: no cover

class MockOpts: # pragma: no cover
    spargs = ['invalid-value'] # pragma: no cover
    output = None # pragma: no cover
    overwrite_output = False # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), {'settings': Settings(), 'process_options': ScrapyCommand.process_options})() # pragma: no cover
args = [] # pragma: no cover
opts = MockOpts() # pragma: no cover
 # pragma: no cover
def feed_process_params_from_cli(settings, output, output_format, overwrite_output): # pragma: no cover
    return {} # pragma: no cover

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
