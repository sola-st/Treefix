# Extracted from https://stackoverflow.com/questions/1260792/import-a-file-from-a-subdirectory
 init():
   print('Hello world!')

import create_card

create_card.init()

from create_card import init

