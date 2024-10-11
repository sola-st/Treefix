import sys # pragma: no cover
import os # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
from l3.Runtime import _l_
sys.path.append(os.path.dirname(os.getcwd()))
_l_(12158)

sys.path.insert(1, os.path.dirname(os.getcwd()))
_l_(12159)

