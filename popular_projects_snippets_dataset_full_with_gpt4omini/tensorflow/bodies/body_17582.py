# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_test.py
with ops.Graph().as_default() as g:
    with ops.device('gpu:0'):
        variable_scope.get_variable(
            name='v', shape=[8, 2], initializer=init_ops.Orthogonal)
        variable_scope.get_variable(
            name='w', shape=[8, 2], initializer=init_ops.RandomNormal)
    run_metadata = config_pb2.RunMetadata()
    run_options = config_pb2.RunOptions(
        trace_level=config_pb2.RunOptions.FULL_TRACE)
    config = config_pb2.ConfigProto(
        allow_soft_placement=False, log_device_placement=True)

    # Note: allow_soft_placement=False will fail whenever we cannot satisfy
    # the colocation constraints.
    with session.Session(config=config, graph=g) as sess:
        sess.run(
            variables.global_variables_initializer(),
            options=run_options,
            run_metadata=run_metadata)
