# Extracted from ./data/repos/tensorflow/tensorflow/python/util/protobuf/compare.py
"""Fails with a useful error if a and b aren't equal.

  Comparison of repeated fields matches the semantics of
  unittest.TestCase.assertEqual(), ie order and extra duplicates fields matter.

  Args:
    self: googletest.TestCase
    a: proto2 PB instance, or text string representing one.
    b: proto2 PB instance -- message.Message or subclass thereof.
    check_initialized: boolean, whether to fail if either a or b isn't
      initialized.
    normalize_numbers: boolean, whether to normalize types and precision of
      numbers before comparison.
    msg: if specified, is used as the error message on failure.
  """
pool = descriptor_pool.Default()
if isinstance(a, six.string_types):
    a = text_format.Merge(a, b.__class__(), descriptor_pool=pool)

for pb in a, b:
    if check_initialized:
        errors = pb.FindInitializationErrors()
        if errors:
            self.fail('Initialization errors: %s\n%s' % (errors, pb))
    if normalize_numbers:
        NormalizeNumberFields(pb)

a_str = text_format.MessageToString(a, descriptor_pool=pool)
b_str = text_format.MessageToString(b, descriptor_pool=pool)

# Some Python versions would perform regular diff instead of multi-line
# diff if string is longer than 2**16. We substitute this behavior
# with a call to unified_diff instead to have easier-to-read diffs.
# For context, see: https://bugs.python.org/issue11763.
if len(a_str) < 2**16 and len(b_str) < 2**16:
    self.assertMultiLineEqual(a_str, b_str, msg=msg)
else:
    diff = ''.join(
        difflib.unified_diff(a_str.splitlines(True), b_str.splitlines(True)))
    if diff:
        self.fail('%s :\n%s' % (msg, diff))
