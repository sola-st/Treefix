# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/giant_const_op_test.py
super(GiantConstOp, self).setUp()
# Make sure TF_XLA_FLAGS is not already set to avoid dropping the existing
# value silently.
assert "TF_XLA_FLAGS" not in os.environ

# Disable tfxla constant folding that always creates full Tensors and will
# fail for giant tensors.
os.environ["TF_XLA_FLAGS"] = "--tf_xla_disable_constant_folding=true"
