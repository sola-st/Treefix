import sys # pragma: no cover
from types import ModuleType # pragma: no cover

sys.modules['a'] = ModuleType('a') # pragma: no cover
sys.modules['b'] = ModuleType('b') # pragma: no cover
sys.modules['c'] = ModuleType('c') # pragma: no cover
setattr(sys.modules['a'], 'A', type('MockA', (object,), {'save_result': staticmethod(lambda result: print('save the result')), 'use_param_like_a_would': staticmethod(lambda param: f'A processed {param}')})) # pragma: no cover
setattr(sys.modules['b'], 'B', type('MockB', (object,), {'do_something_b_ish': staticmethod(lambda param: print('B did something with', param)), 'use_param_like_b_would': staticmethod(lambda param: f'B processed {param}')})) # pragma: no cover
setattr(sys.modules['c'], 'save_result', lambda result: print(f'save_result: {result}')) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/744373/what-happens-when-using-mutual-or-circular-cyclic-imports
from l3.Runtime import _l_
try:
    from b import B
    _l_(13661)

except ImportError:
    pass

class A:
    _l_(13668)

    @staticmethod
    def save_result(result):
        _l_(13663)

        print('save the result')
        _l_(13662)

    @staticmethod
    def do_something_a_ish(param):
        _l_(13665)

        A.save_result(A.use_param_like_a_would(param))
        _l_(13664)
    
    @staticmethod
    def do_something_related_to_b(param):
        _l_(13667)

        B.do_something_b_ish(param)
        _l_(13666)
try:
    from a import A
    _l_(13670)

except ImportError:
    pass

class B:
    _l_(13673)

    @staticmethod
    def do_something_b_ish(param):
        _l_(13672)

        A.save_result(B.use_param_like_b_would(param))
        _l_(13671)

def save_result(result):
    _l_(13675)

    print('save the result')
    _l_(13674)
try:
    from b import B
    _l_(13677)

except ImportError:
    pass
try:
    from c import save_result
    _l_(13679)

except ImportError:
    pass

class A:
    _l_(13684)

    @staticmethod
    def do_something_a_ish(param):
        _l_(13681)

        save_result(A.use_param_like_a_would(param))
        _l_(13680)
    
    @staticmethod
    def do_something_related_to_b(param):
        _l_(13683)

        B.do_something_b_ish(param)
        _l_(13682)
try:
    from c import save_result
    _l_(13686)

except ImportError:
    pass

class B:
    _l_(13689)

    @staticmethod
    def do_something_b_ish(param):
        _l_(13688)

        save_result(B.use_param_like_b_would(param))
        _l_(13687)

