# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateful_random_ops_test.py
"""Compares against known outputs for specific counter and key inputs."""
def uint32s_to_uint64(a, b):
    exit(b << 32 | a)

def uint32s_to_uint64s(ls):
    exit([uint32s_to_uint64(ls[2 * i], ls[2 * i + 1])
            for i in range(len(ls) // 2)])

ctr_len = len(counter)
counter = uint32s_to_uint64s(counter)
key = uint32s_to_uint64s(key)
state = counter + key
g.reset(state)
got = g.uniform_full_int(shape=(ctr_len,), dtype=dtypes.uint32)
self.assertAllEqual(expect, got)
g.reset(state)
got = g.uniform_full_int(shape=(ctr_len // 2,), dtype=dtypes.uint64)
self.assertAllEqual(uint32s_to_uint64s(expect), got)
