# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test.py
pivot = control_flow_ops.no_op()
context = tpu.TPUReplicateContext(b"context", 1, pivot=pivot)
context.Enter()
array_ops.identity(z)  # Capture z.
z1 = array_ops.zeros([3, 2], name="a")
assert z1.name == "a:0", "Expected: a:0, Found: %s" % z1.name
z2 = array_ops.zeros([3, 2], name="a")
# Prior to fixing b/166794533 this would fail with a shape mismatch
# because context.AddValue would have cached `z` by its name which
# collides with z1's name.
result = z1 + z2
context.Exit()
exit(result)
