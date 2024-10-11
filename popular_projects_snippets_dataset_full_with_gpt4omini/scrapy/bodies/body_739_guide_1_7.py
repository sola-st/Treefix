from scrapy.commands import ScrapyCommand # pragma: no cover
from scrapy.exceptions import UsageError # pragma: no cover

self = type('MockScrapyCommand', (ScrapyCommand,), {'settings': {}})() # pragma: no cover
args = [] # pragma: no cover
opts = type('MockOptions', (object,), {'spargs': ['key=value'], 'output': 'output.json', 'output_format': 'json', 'overwrite_output': False})() # pragma: no cover

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
