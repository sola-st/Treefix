# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/commands/__init__.py
from l3.Runtime import _l_
"""
        Populate option parse with options available for this command
        """
group = parser.add_argument_group(title='Global Options')
_l_(21107)
group.add_argument("--logfile", metavar="FILE",
                   help="log file. if omitted stderr will be used")
_l_(21108)
group.add_argument("-L", "--loglevel", metavar="LEVEL", default=None,
                   help=f"log level (default: {self.settings['LOG_LEVEL']})")
_l_(21109)
group.add_argument("--nolog", action="store_true",
                   help="disable logging completely")
_l_(21110)
group.add_argument("--profile", metavar="FILE", default=None,
                   help="write python cProfile stats to FILE")
_l_(21111)
group.add_argument("--pidfile", metavar="FILE",
                   help="write process ID to FILE")
_l_(21112)
group.add_argument("-s", "--set", action="append", default=[], metavar="NAME=VALUE",
                   help="set/override setting (may be repeated)")
_l_(21113)
group.add_argument("--pdb", action="store_true", help="enable pdb on failure")
_l_(21114)
