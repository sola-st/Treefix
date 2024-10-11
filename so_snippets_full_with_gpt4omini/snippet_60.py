# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
from l3.Runtime import _l_
sys.path.append('c:\\tools\\mydir')
_l_(1573)
sys.path.append('..\\mytools')
_l_(1574)
sys.path.append('c:/tools/mydir')
_l_(1575)
sys.path.append('../mytools')
_l_(1576)

