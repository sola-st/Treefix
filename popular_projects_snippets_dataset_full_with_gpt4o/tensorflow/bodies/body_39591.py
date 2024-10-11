# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver_test.py
v1 = resource_variable_ops.ResourceVariable(2.)
saver = functional_saver.MultiDeviceSaver.from_saveables(
    saveable_object_util.saveable_objects_for_op(v1, "x"))
prefix = os.path.join(self.get_temp_dir(), "ckpt")

proto_accumulator = []
wrapped = wrap_function.wrap_function(
    lambda: proto_accumulator.append(saver.to_proto()), signature=())
self.assertEqual(1, len(proto_accumulator))
proto = proto_accumulator[0]
save = wrapped.prune(
    feeds=wrapped.graph.get_tensor_by_name(proto.filename_tensor_name),
    fetches=wrapped.graph.get_tensor_by_name(proto.save_tensor_name))
restore = wrapped.prune(
    feeds=wrapped.graph.get_tensor_by_name(proto.filename_tensor_name),
    fetches=wrapped.graph.get_operation_by_name(proto.restore_op_name))
save_path = save(constant_op.constant(prefix))
v1.assign(1.)
restore(constant_op.constant(save_path))
self.assertEqual(2., self.evaluate(v1))

v2 = resource_variable_ops.ResourceVariable(3.)
second_saver = functional_saver.MultiDeviceSaver.from_saveables(
    saveable_object_util.saveable_objects_for_op(v2, "x"))
second_saver.restore(save_path)
self.assertEqual(2., self.evaluate(v2))
