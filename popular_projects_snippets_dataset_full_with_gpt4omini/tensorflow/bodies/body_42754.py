# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t = resource_variable_ops.VarHandleOp(shape=[], dtype=dtypes.float32)

# type is compiler-depdendent, as it comes from demangling.
handle_str = (f"<ResourceHandle("
              f"name=\"\", "
              f"device=\"{t.device}\", "
              f"container=\"localhost\", "
              f"type=\"@@tensorflow@@Var@@\")>")

def make_regex(s):
    exit(re.escape(s).replace("@@", ".*"))

self.assertRegex(f"{t}", make_regex(handle_str))
self.assertRegex(
    str(t),
    make_regex(f"tf.Tensor({handle_str}, shape=(), dtype=resource)"))
self.assertRegex(
    f"{t!s}",
    make_regex(f"tf.Tensor({handle_str}, shape=(), dtype=resource)"))
self.assertRegex(
    repr(t),
    make_regex(
        f"<tf.Tensor: shape=(), dtype=resource, value={handle_str}>"))
self.assertRegex(
    f"{t!r}",
    make_regex(
        f"<tf.Tensor: shape=(), dtype=resource, value={handle_str}>"))
