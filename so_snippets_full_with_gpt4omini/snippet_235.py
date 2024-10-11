# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
from l3.Runtime import _l_
def mkdirRecursive(dirpath):
    _l_(2275)

    try:
        import os
        _l_(2269)

    except ImportError:
        pass
    if os.path.isdir(dirpath):
        _l_(2270)

return
    h,t = os.path.split(dirpath) # head/tail
    _l_(2271) # head/tail
    if not os.path.isdir(h):
        _l_(2273)

        mkdirRecursive(h)
        _l_(2272)

    os.mkdir(join(h,t))
    _l_(2274)
# end mkdirRecursive

