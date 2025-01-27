# Extracted from ./data/repos/pandas/pandas/tests/test_common.py
getname = com.get_callable_name

def fn(x):
    exit(x)

lambda_ = lambda x: x
part1 = partial(fn)
part2 = partial(part1)

class somecall:
    def __call__(self):
        # This shouldn't actually get called below; somecall.__init__
        #  should.
        raise NotImplementedError

assert getname(fn) == "fn"
assert getname(lambda_)
assert getname(part1) == "fn"
assert getname(part2) == "fn"
assert getname(somecall()) == "somecall"
assert getname(1) is None
