# Extracted from ./data/repos/scrapy/scrapy/commands/version.py
ScrapyCommand.add_options(self, parser)
parser.add_argument("--verbose", "-v", dest="verbose", action="store_true",
                    help="also display twisted/python/platform info (useful for bug reports)")
