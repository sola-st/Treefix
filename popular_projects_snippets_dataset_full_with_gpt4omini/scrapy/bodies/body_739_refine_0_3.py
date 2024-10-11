from scrapy.commands import ScrapyCommand # pragma: no cover
from scrapy.exceptions import UsageError # pragma: no cover
from scrapy.utils.project import get_project_settings # pragma: no cover

class MockSettings: pass# pragma: no cover
args = [] # pragma: no cover
class MockOpts:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.spargs = {}# pragma: no cover
        self.output = 'output.json'# pragma: no cover
        self.overwrite_output = False# pragma: no cover
        self.output_format = 'json'# pragma: no cover
opts = MockOpts() # pragma: no cover
def arglist_to_dict(spargs): return spargs# pragma: no cover
 # pragma: no cover
def feed_process_params_from_cli(settings, output, output_format, overwrite_output): return { 'file': output, 'format': output_format }# pragma: no cover
 # pragma: no cover

from scrapy.commands import ScrapyCommand # pragma: no cover
from scrapy.exceptions import UsageError # pragma: no cover
from scrapy.utils.project import get_project_settings # pragma: no cover

class MockSettings:# pragma: no cover
    def set(self, key, value, priority): pass# pragma: no cover
class MockSelf:# pragma: no cover
    pass
self = MockSelf() # pragma: no cover
args = [] # pragma: no cover
class MockOpts:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.spargs = {}# pragma: no cover
        self.output = 'output.json'# pragma: no cover
        self.overwrite_output = False# pragma: no cover
        self.output_format = 'json'# pragma: no cover
opts = MockOpts() # pragma: no cover
def arglist_to_dict(spargs): return spargs# pragma: no cover
 # pragma: no cover
def feed_process_params_from_cli(settings, output, output_format, overwrite_output): return { 'file': output, 'format': output_format }# pragma: no cover
 # pragma: no cover

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
