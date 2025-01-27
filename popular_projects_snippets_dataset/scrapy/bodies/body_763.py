# Extracted from ./data/repos/scrapy/scrapy/commands/parse.py
BaseRunSpiderCommand.add_options(self, parser)
parser.add_argument("--spider", dest="spider", default=None,
                    help="use this spider without looking for one")
parser.add_argument("--pipelines", action="store_true",
                    help="process items through pipelines")
parser.add_argument("--nolinks", dest="nolinks", action="store_true",
                    help="don't show links to follow (extracted requests)")
parser.add_argument("--noitems", dest="noitems", action="store_true",
                    help="don't show scraped items")
parser.add_argument("--nocolour", dest="nocolour", action="store_true",
                    help="avoid using pygments to colorize the output")
parser.add_argument("-r", "--rules", dest="rules", action="store_true",
                    help="use CrawlSpider rules to discover the callback")
parser.add_argument("-c", "--callback", dest="callback",
                    help="use this callback for parsing, instead looking for a callback")
parser.add_argument("-m", "--meta", dest="meta",
                    help="inject extra meta into the Request, it must be a valid raw json string")
parser.add_argument("--cbkwargs", dest="cbkwargs",
                    help="inject extra callback kwargs into the Request, it must be a valid raw json string")
parser.add_argument("-d", "--depth", dest="depth", type=int, default=1,
                    help="maximum depth for parsing requests [default: %(default)s]")
parser.add_argument("-v", "--verbose", dest="verbose", action="store_true",
                    help="print each depth level one by one")
