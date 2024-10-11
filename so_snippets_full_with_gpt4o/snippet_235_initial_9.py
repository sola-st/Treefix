from os.path import join # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
from l3.Runtime import _l_
def mkdirRecursive(dirpath):
    _l_(13710)

    try:
        import os
        _l_(13704)

    except ImportError:
        pass
    if os.path.isdir(dirpath):
        _l_(13705)

return
    h,t = os.path.split(dirpath) # head/tail
    _l_(13706) # head/tail
    if not os.path.isdir(h):
        _l_(13708)

        mkdirRecursive(h)
        _l_(13707)

    os.mkdir(join(h,t))
    _l_(13709)
# end mkdirRecursive

