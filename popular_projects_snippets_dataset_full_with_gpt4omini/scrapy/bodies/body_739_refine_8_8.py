from scrapy.commands import ScrapyCommand # pragma: no cover
from scrapy.exceptions import UsageError # pragma: no cover

from scrapy.commands import ScrapyCommand # pragma: no cover
from scrapy.exceptions import UsageError # pragma: no cover

class MockSettings:# pragma: no cover
    def set(self, key, value, priority): pass # pragma: no cover
class MockOpts:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.spargs = 'key=value'# pragma: no cover
        self.output = 'output.json'# pragma: no cover
        self.overwrite_output = True# pragma: no cover
        self.output_format = 'json' # pragma: no cover
self = type('MockSelf', (), {'settings': MockSettings()})() # pragma: no cover
args = [] # pragma: no cover
opts = MockOpts() # pragma: no cover
arglist_to_dict = lambda spargs: {item.split('=')[0]: item.split('=')[1] for item in spargs.split(',')} # pragma: no cover
feed_process_params_from_cli = lambda settings, output, output_format, overwrite_output: {'uri': output, 'format': output_format, 'overwrite': overwrite_output} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/commands/__init__.py
from l3.Runtime import _l_
ScrapyCommand.process_options(self, args, opts)
_l_(6812)
try:
    _l_(6816)

    opts.spargs = arglist_to_dict(opts.spargs)
    _l_(6813)
except ValueError:
    _l_(6815)

    raise UsageError("Invalid -a value, use -a NAME=VALUE", print_help=False)
    _l_(6814)
if opts.output or opts.overwrite_output:
    _l_(6819)

    feeds = feed_process_params_from_cli(
        self.settings,
        opts.output,
        opts.output_format,
        opts.overwrite_output,
    )
    _l_(6817)
    self.settings.set('FEEDS', feeds, priority='cmdline')
    _l_(6818)
