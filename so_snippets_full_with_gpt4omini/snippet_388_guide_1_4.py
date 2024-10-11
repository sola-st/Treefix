from unittest.mock import patch # pragma: no cover

raw_input = patch('builtins.input', side_effect=['n']).start() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/189645/how-can-i-break-out-of-multiple-loops
from l3.Runtime import _l_
while True:
    _l_(2871)

    break_statement=0
    _l_(2861)
    while True:
        _l_(2868)

        ok = raw_input("Is this ok? (y/n)")
        _l_(2862)
        if ok == "n" or ok == "N":
            _l_(2864)

            break
            _l_(2863)
        if ok == "y" or ok == "Y":
            _l_(2867)

            break_statement=1
            _l_(2865)
            break
            _l_(2866)
    if break_statement==1:
        _l_(2870)

        break
        _l_(2869)

