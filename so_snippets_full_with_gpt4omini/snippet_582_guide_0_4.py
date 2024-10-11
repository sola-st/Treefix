class MockB(object): # pragma: no cover
    @staticmethod # pragma: no cover
    def use_param_like_b_would(param): return param * 2 # pragma: no cover
    @staticmethod # pragma: no cover
    def do_something_b_ish(param): save_result(MockB.use_param_like_b_would(param)) # pragma: no cover
B = MockB # pragma: no cover
class MockA(object): # pragma: no cover
    @staticmethod # pragma: no cover
    def use_param_like_a_would(param): return param + 1 # pragma: no cover
    @staticmethod # pragma: no cover
    def save_result(result): print('save the result') # pragma: no cover
    @staticmethod # pragma: no cover
    def do_something_a_ish(param): MockA.save_result(MockA.use_param_like_a_would(param)) # pragma: no cover
A = MockA # pragma: no cover
def save_result(result): print('save the result') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/744373/what-happens-when-using-mutual-or-circular-cyclic-imports
from l3.Runtime import _l_
try:
    from b import B
    _l_(3365)

except ImportError:
    pass

class A:
    _l_(3372)

    @staticmethod
    def save_result(result):
        _l_(3367)

        print('save the result')
        _l_(3366)

    @staticmethod
    def do_something_a_ish(param):
        _l_(3369)

        A.save_result(A.use_param_like_a_would(param))
        _l_(3368)
    
    @staticmethod
    def do_something_related_to_b(param):
        _l_(3371)

        B.do_something_b_ish(param)
        _l_(3370)
try:
    from a import A
    _l_(3374)

except ImportError:
    pass

class B:
    _l_(3377)

    @staticmethod
    def do_something_b_ish(param):
        _l_(3376)

        A.save_result(B.use_param_like_b_would(param))
        _l_(3375)

def save_result(result):
    _l_(3379)

    print('save the result')
    _l_(3378)
try:
    from b import B
    _l_(3381)

except ImportError:
    pass
try:
    from c import save_result
    _l_(3383)

except ImportError:
    pass

class A:
    _l_(3388)

    @staticmethod
    def do_something_a_ish(param):
        _l_(3385)

        save_result(A.use_param_like_a_would(param))
        _l_(3384)
    
    @staticmethod
    def do_something_related_to_b(param):
        _l_(3387)

        B.do_something_b_ish(param)
        _l_(3386)
try:
    from c import save_result
    _l_(3390)

except ImportError:
    pass

class B:
    _l_(3393)

    @staticmethod
    def do_something_b_ish(param):
        _l_(3392)

        save_result(B.use_param_like_b_would(param))
        _l_(3391)

