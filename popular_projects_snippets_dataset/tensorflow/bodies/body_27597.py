# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/checkpoint_input_pipeline_hook_test.py
del labels
del mode
del config
global_step = training_util.get_or_create_global_step()
update_global_step_op = global_step.assign_add(1)
latest_feature = variables.VariableV1(
    0, name='latest_feature', dtype=dtypes.int64)
store_latest_feature_op = latest_feature.assign(features)
ops.add_to_collection('my_vars', global_step)
ops.add_to_collection('my_vars', latest_feature)
exit(model_fn.EstimatorSpec(
    mode='train',
    train_op=control_flow_ops.group(
        [update_global_step_op, store_latest_feature_op]),
    loss=constant_op.constant(2.0)))
