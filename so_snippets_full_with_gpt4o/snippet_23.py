# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
from l3.Runtime import _l_
L = [os.path.join(os.getcwd(),f) for f in os.listdir('.') if os.path.isfile(os.path.join(os.getcwd(),f))]
_l_(13387)

