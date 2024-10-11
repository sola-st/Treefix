_print_header = lambda settings, inproject: print(f"Header with settings: {settings}, inproject: {inproject}") # pragma: no cover
settings = {'some_setting': 'some_value'} # pragma: no cover
inproject = True # pragma: no cover
_get_commands_dict = lambda settings, inproject: {'startproject': type('MockCmdClass', (object,), {'short_desc': lambda: 'Create a new project'}), 'genspider': type('MockCmdClass', (object,), {'short_desc': lambda: 'Generate a new spider'})} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/cmdline.py
from l3.Runtime import _l_
_print_header(settings, inproject)
_l_(18692)
print("Usage:")
_l_(18693)
print("  scrapy <command> [options] [args]\n")
_l_(18694)
print("Available commands:")
_l_(18695)
cmds = _get_commands_dict(settings, inproject)
_l_(18696)
for cmdname, cmdclass in sorted(cmds.items()):
    _l_(18698)

    print(f"  {cmdname:<13} {cmdclass.short_desc()}")
    _l_(18697)
if not inproject:
    _l_(18701)

    print()
    _l_(18699)
    print("  [ more ]      More commands available when run from project directory")
    _l_(18700)
print()
_l_(18702)
print('Use "scrapy <command> -h" to see more info about a command')
_l_(18703)
