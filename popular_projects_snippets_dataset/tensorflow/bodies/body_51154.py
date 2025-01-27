# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_test.py
receiver_tensor = constant_op.constant(["11"])

with self.assertRaises(ValueError) as e:
    export_utils.build_all_signature_defs(receiver_tensor, None)

self.assertTrue(
    str(e.exception).startswith("`export_outputs` must be a dict"))
