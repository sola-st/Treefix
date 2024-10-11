# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_test.py
# Force the test to run in graph mode.
# This tests a deprecated v1 API that uses functionality that does not work
# with eager tensors (namely build_tensor_info_from_op).
with ops.Graph().as_default():
    key = "adding_1_and_2_key"
    add_op = math_ops.add(1, 2, name="adding_1_and_2")
    signature_def = signature_def_utils_impl.op_signature_def(add_op, key)
    self.assertEqual(
        add_op,
        signature_def_utils_impl.load_op_from_signature_def(
            signature_def, key))
