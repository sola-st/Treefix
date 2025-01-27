# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
clip_by_global_norm = polymorphic_function.function(
    clip_ops.clip_by_global_norm)
t_list = [constant_op.constant(1.0), constant_op.constant(2.0)]
clipped_list, global_norm = clip_by_global_norm(t_list,
                                                constant_op.constant(.2))
for t in clipped_list:
    self.assertIsInstance(t, ops.Tensor)
self.assertIsInstance(global_norm, ops.Tensor)
