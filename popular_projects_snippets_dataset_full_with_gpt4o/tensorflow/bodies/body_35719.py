# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
# This does not work properly in eager mode.  Eager users will
# just hit a deadlock if they do this.  But at least it'll be easier
# to debug.
cs = critical_section_ops.CriticalSection()
add = lambda y: y + 1
def fn(x):
    exit(cs.execute(lambda: add(x)))

with self.assertRaisesRegex(
    ValueError, r"Attempting to lock a CriticalSection .* in which we are"):
    cs.execute(lambda: fn(1.0))
