# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/decode_proto_op_test_base.py
"""Compare lists/arrays of field values."""

if len(vs) != len(evs):
    self.fail('Field %s decoded %d outputs, expected %d' %
              (fd.name, len(vs), len(evs)))
for i, ev in enumerate(evs):
    # Special case fuzzy match for float32. TensorFlow seems to mess with
    # MAX_FLT slightly and the test doesn't work otherwise.
    # TODO(nix): ask on TF list about why MAX_FLT doesn't pass through.
    if fd.cpp_type == fd.CPPTYPE_FLOAT:
        # Numpy isclose() is better than assertIsClose() which uses an absolute
        # value comparison.
        self.assertTrue(
            np.isclose(vs[i], ev), 'expected %r, actual %r' % (ev, vs[i]))
    elif fd.cpp_type == fd.CPPTYPE_STRING:
        # In Python3 string tensor values will be represented as bytes, so we
        # reencode the proto values to match that.
        self.assertEqual(vs[i], ev.encode('ascii'))
    else:
        # Doubles and other types pass through unscathed.
        self.assertEqual(vs[i], ev)
