from typing import Dict, Type, Any # pragma: no cover

_print_header = lambda settings, inproject: print('Header:', settings)  # Mock function to print header # pragma: no cover
settings = {'project_name': 'MyScrapyProject', 'version': '1.0', 'author': 'AuthorName'} # pragma: no cover
inproject = True # pragma: no cover
_get_commands_dict = lambda settings, inproject: {'startproject': type('MockCmd', (), {'short_desc': staticmethod(lambda: 'Creates a new Scrapy project')}), 'crawl': type('MockCmd', (), {'short_desc': staticmethod(lambda: 'Crawls a website')})} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/cmdline.py
from l3.Runtime import _l_
_print_header(settings, inproject)
_l_(7933)
print("Usage:")
_l_(7934)
print("  scrapy <command> [options] [args]\n")
_l_(7935)
print("Available commands:")
_l_(7936)
cmds = _get_commands_dict(settings, inproject)
_l_(7937)
for cmdname, cmdclass in sorted(cmds.items()):
    _l_(7939)

    print(f"  {cmdname:<13} {cmdclass.short_desc()}")
    _l_(7938)
if not inproject:
    _l_(7942)

    print()
    _l_(7940)
    print("  [ more ]      More commands available when run from project directory")
    _l_(7941)
print()
_l_(7943)
print('Use "scrapy <command> -h" to see more info about a command')
_l_(7944)
