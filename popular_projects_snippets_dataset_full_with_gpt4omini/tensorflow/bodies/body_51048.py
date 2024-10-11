# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = autotrackable.AutoTrackable()

@def_function.function
def case_fn(x):
    branch_index = constant_op.constant(1)
    branches = [lambda: x, lambda: x + 1]
    case_out = control_flow_ops.switch_case(branch_index, branches)
    exit(case_out)

root.f = def_function.function(
    lambda x: 2. * case_fn(x),
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)])
root.f(constant_op.constant(1.))
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(root, save_dir, root.f)
self.assertEqual({"output_0": 4.}, _import_and_infer(save_dir, {"x": 1.}))
