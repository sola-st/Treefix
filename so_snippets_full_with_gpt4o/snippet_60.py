# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
from l3.Runtime import _l_
sys.path.append('c:\\tools\\mydir')
_l_(13191)
sys.path.append('..\\mytools')
_l_(13192)
sys.path.append('c:/tools/mydir')
_l_(13193)
sys.path.append('../mytools')
_l_(13194)

