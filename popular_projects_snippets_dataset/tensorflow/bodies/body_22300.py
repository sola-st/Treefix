# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer_test.py
v = variables.Variable([1.0])
self.assertTrue(distribute_utils.is_distributed_variable(v))
# Slot variables are created in the first call to apply_gradients.
optimizer.apply_gradients([(ops.convert_to_tensor([1.0]), v)])
self.assertTrue(optimizer.get_slot_names())
for name in optimizer.get_slot_names():
    slot = optimizer.get_slot(v, name)
    self.assertIsNotNone(slot)
    self.assertTrue(distribute_utils.is_distributed_variable(slot))
