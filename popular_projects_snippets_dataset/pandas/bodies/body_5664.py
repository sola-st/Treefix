# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 13445
# numpy's argsort can be unhappy if something is less than
# itself.  Instead, let's give our infinities a self-consistent
# ordering, but outside the float extended real line.

Inf = libalgos.Infinity()
NegInf = libalgos.NegInfinity()

ref_nums = [NegInf, float("-inf"), -1e100, 0, 1e100, float("inf"), Inf]

assert all(Inf >= x for x in ref_nums)
assert all(Inf > x or x is Inf for x in ref_nums)
assert Inf >= Inf and Inf == Inf
assert not Inf < Inf and not Inf > Inf
assert libalgos.Infinity() == libalgos.Infinity()
assert not libalgos.Infinity() != libalgos.Infinity()

assert all(NegInf <= x for x in ref_nums)
assert all(NegInf < x or x is NegInf for x in ref_nums)
assert NegInf <= NegInf and NegInf == NegInf
assert not NegInf < NegInf and not NegInf > NegInf
assert libalgos.NegInfinity() == libalgos.NegInfinity()
assert not libalgos.NegInfinity() != libalgos.NegInfinity()

for perm in permutations(ref_nums):
    assert sorted(perm) == ref_nums

# smoke tests
np.array([libalgos.Infinity()] * 32).argsort()
np.array([libalgos.NegInfinity()] * 32).argsort()
