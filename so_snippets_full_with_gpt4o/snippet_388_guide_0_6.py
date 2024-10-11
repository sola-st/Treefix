def raw_input(prompt): # pragma: no cover
    return 'y' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/189645/how-can-i-break-out-of-multiple-loops
from l3.Runtime import _l_
while True:
    _l_(15045)

    break_statement=0
    _l_(15035)
    while True:
        _l_(15042)

        ok = raw_input("Is this ok? (y/n)")
        _l_(15036)
        if ok == "n" or ok == "N":
            _l_(15038)

            break
            _l_(15037)
        if ok == "y" or ok == "Y":
            _l_(15041)

            break_statement=1
            _l_(15039)
            break
            _l_(15040)
    if break_statement==1:
        _l_(15044)

        break
        _l_(15043)

