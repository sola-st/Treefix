# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2225564/get-a-filtered-list-of-files-in-a-directory
from l3.Runtime import _l_
files = [f for f in os.listdir('.') if re.match(r'[0-9]+.*\.jpg', f)]
_l_(12648)

