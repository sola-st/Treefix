from scrapy.commands import ScrapyCommand # pragma: no cover
from scrapy.exceptions import UsageError # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
args = [] # pragma: no cover
opts = type('Mock', (object,), {'spargs': ['invalid_arg'], 'output': None, 'overwrite_output': None, 'output_format': None})() # pragma: no cover
self.settings = type('Mock', (object,), {'set': lambda *args, **kwargs: None})() # pragma: no cover

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
