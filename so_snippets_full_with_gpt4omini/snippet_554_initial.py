# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters
from l3.Runtime import _l_
try:
    import sys
    _l_(1878)

except ImportError:
    pass

sys.stdout.write("-") # prints a dash for each iteration of loop
_l_(1879) # prints a dash for each iteration of loop
sys.stdout.flush() # ensures bar is displayed incrementally
_l_(1880) # ensures bar is displayed incrementally

