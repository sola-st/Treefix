from unittest.mock import Mock # pragma: no cover
from scrapy.exceptions import UsageError # pragma: no cover

ScrapyCommand = Mock() # pragma: no cover
ScrapyCommand.process_options = Mock() # pragma: no cover
self = Mock() # pragma: no cover
self.settings = Mock() # pragma: no cover
self.settings.set = Mock() # pragma: no cover
args = [] # pragma: no cover
opts = Mock() # pragma: no cover
opts.spargs = [] # pragma: no cover
opts.output = 'output_file.json' # pragma: no cover
opts.overwrite_output = True # pragma: no cover
opts.output_format = 'json' # pragma: no cover
arglist_to_dict = lambda x: {item.split('=')[0]: item.split('=')[1] for item in x} # pragma: no cover
feed_process_params_from_cli = Mock(return_value={'FEEDS': 'processed_feed'}) # pragma: no cover

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
