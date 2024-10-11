import traceback # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4564559/get-exception-description-and-stack-trace-which-caused-an-exception-all-as-a-st
from l3.Runtime import _l_
try:
    _l_(1130)

    ...
    _l_(1127)
except Exception as e:
    _l_(1129)

    print(traceback.print_tb(e.__traceback__))
    _l_(1128)

