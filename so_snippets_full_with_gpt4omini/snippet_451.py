# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4934806/how-can-i-find-scripts-directory
from l3.Runtime import _l_
try:
    import os
    _l_(1962)

except ImportError:
    pass
exec_filepath = os.path.realpath(__file__)
_l_(1963)
exec_dirpath = exec_filepath[0:len(exec_filepath)-len(os.path.basename(__file__))]
_l_(1964)

