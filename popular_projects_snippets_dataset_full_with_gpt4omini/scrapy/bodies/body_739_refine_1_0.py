from scrapy.commands import ScrapyCommand # pragma: no cover
from scrapy.exceptions import UsageError # pragma: no cover
from scrapy.settings import Settings # pragma: no cover

class Mock: pass # pragma: no cover
ScrapyCommand = type('MockScrapyCommand', (ScrapyCommand,), {}) # pragma: no cover
self = Mock() # pragma: no cover
args = ['--arg1', 'value1'] # pragma: no cover
class MockOpts: pass # pragma: no cover
opts = MockOpts() # pragma: no cover
opts.spargs = 'arg1=value1,arg2=value2' # pragma: no cover
opts.output = 'output.json' # pragma: no cover
opts.overwrite_output = True # pragma: no cover
opts.output_format = 'json' # pragma: no cover
def arglist_to_dict(spargs): return dict(item.split('=') for item in spargs.split(',')) # pragma: no cover
def feed_process_params_from_cli(settings, output, output_format, overwrite_output): return {'format': output_format, 'uri': output, 'overwrite': overwrite_output} # pragma: no cover
self.settings = Settings() # pragma: no cover

from scrapy.commands import ScrapyCommand # pragma: no cover
from scrapy.exceptions import UsageError # pragma: no cover
from scrapy.utils.project import get_project_settings # pragma: no cover
from scrapy.settings import Settings # pragma: no cover

class Mock: pass # pragma: no cover
ScrapyCommand = type('MockScrapyCommand', (ScrapyCommand,), {}) # pragma: no cover
self = Mock() # pragma: no cover
args = ['--arg1', 'value1'] # pragma: no cover
class MockOpts: pass # pragma: no cover
opts = MockOpts() # pragma: no cover
opts.spargs = 'arg1=value1,arg2=value2' # pragma: no cover
opts.output = 'output.json' # pragma: no cover
opts.overwrite_output = True # pragma: no cover
opts.output_format = 'json' # pragma: no cover
def arglist_to_dict(spargs): return dict(item.split('=') for item in spargs.split(',')) # pragma: no cover
def feed_process_params_from_cli(settings, output, output_format, overwrite_output): return {'format': output_format, 'uri': output, 'overwrite': overwrite_output} # pragma: no cover
self.settings = Settings() # pragma: no cover
self.settings.setdict = lambda x, priority: None # pragma: no cover

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
