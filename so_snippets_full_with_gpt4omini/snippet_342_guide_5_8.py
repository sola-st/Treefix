# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/256222/which-exception-should-i-raise-on-bad-illegal-argument-combinations-in-python
from l3.Runtime import _l_
def import_to_orm(name, save=False, recurse=False):
    _l_(47)

    if recurse and not save:
        _l_(46)

        raise ValueError("save must be True if recurse is True")
        _l_(45)

