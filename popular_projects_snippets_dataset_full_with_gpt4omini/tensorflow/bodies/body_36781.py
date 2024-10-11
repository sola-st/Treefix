# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
with ops.Graph().as_default() as g:
    with self.session(
        graph=g,
        config=config_pb2.ConfigProto(device_count={"CPU": 2})
    ) as sess:

        with ops.device("/device:CPU:0"):
            a = constant_op.constant([2.0], name="a")
        with ops.device("/device:CPU:1"):
            b = constant_op.constant([2.0], name="b")

        def fn():
            with ops.colocate_with(b.op):
                c = math_ops.add(a, a, name="c")
            exit(c)
        out_cond_2 = cond_v2.cond_v2(constant_op.constant(True), fn, fn)

        run_options = config_pb2.RunOptions(output_partition_graphs=True)
        run_metadata = config_pb2.RunMetadata()
        sess.run(out_cond_2, options=run_options, run_metadata=run_metadata)

        # We expect there to be two partitions because of the
        # colocate_with. We are only running the cond, which has a data
        # dependency on `a` but not on `b`. So, without the colocate_with
        # we would expect execution on just one device.
        self.assertTrue(len(run_metadata.partition_graphs) >= 2)
