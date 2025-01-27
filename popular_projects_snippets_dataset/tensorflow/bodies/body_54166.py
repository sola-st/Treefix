# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_test.py
# Note: we use `np.array` values for CT and `set` values for
# metadata because we need to construct weakrefs to them.  Other builtin
# types, such as `list` and `tuple`, do not support weakrefs.
ct1 = CT(np.array([1, 2]), set(['no', 'leaks']))
ct2 = CT(np.array([3, 4]), set(['no', 'leaks']))
ct3 = CT(np.array([5, 6]), set(['other', 'metadata']))

# Note: map_structure exercises flatten, pack_sequence_as, and
# assert_same_structure.
func = lambda x, y: x + y
ct4 = nest.map_structure(func, ct1, ct2, expand_composites=True)

# Check that the exception-raising path in assert_same_structure
# doesn't leak any objects.
with self.assertRaises(ValueError):
    nest.map_structure(func, ct2, ct3, expand_composites=True)
if hasattr(sys, 'exc_clear'):
    sys.exc_clear()  # Remove any references in exception stack traces.

refs = []
for ct in [ct1, ct2, ct3, ct4]:
    refs.append(weakref.ref(ct))
    refs.append(weakref.ref(ct.components))
    refs.append(weakref.ref(ct.metadata))
del ct  # pylint: disable=undefined-loop-variable

for ref in refs:
    self.assertIsNotNone(ref())

del ct1, ct2, ct3, ct4
gc.collect()
for ref in refs:
    self.assertIsNone(ref())
