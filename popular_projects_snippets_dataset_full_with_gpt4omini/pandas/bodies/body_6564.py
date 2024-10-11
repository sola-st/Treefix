# Extracted from ./data/repos/pandas/pandas/tests/test_common.py
import numpy.random as npr

# Check with seed
state = com.random_state(5)
assert state.uniform() == npr.RandomState(5).uniform()

# Check with random state object
state2 = npr.RandomState(10)
assert com.random_state(state2).uniform() == npr.RandomState(10).uniform()

# check with no arg random state
assert com.random_state() is np.random

# check array-like
# GH32503
state_arr_like = npr.randint(0, 2**31, size=624, dtype="uint32")
assert (
    com.random_state(state_arr_like).uniform()
    == npr.RandomState(state_arr_like).uniform()
)

# Check BitGenerators
# GH32503
assert (
    com.random_state(npr.MT19937(3)).uniform()
    == npr.RandomState(npr.MT19937(3)).uniform()
)
assert (
    com.random_state(npr.PCG64(11)).uniform()
    == npr.RandomState(npr.PCG64(11)).uniform()
)

# Error for floats or strings
msg = (
    "random_state must be an integer, array-like, a BitGenerator, Generator, "
    "a numpy RandomState, or None"
)
with pytest.raises(ValueError, match=msg):
    com.random_state("test")

with pytest.raises(ValueError, match=msg):
    com.random_state(5.5)
