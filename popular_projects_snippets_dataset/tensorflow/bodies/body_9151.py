# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
ops.reset_default_graph()
dev = '/device:GPU:0' if test.is_gpu_available() else '/device:CPU:0'
outfile = os.path.join(test.get_temp_dir(), 'dump')
opts = (
    builder(builder.trainable_variables_parameter()).with_file_output(
        outfile).with_accounted_types(['.*']).select([
            'micros', 'bytes', 'params', 'float_ops', 'occurrence',
            'device', 'op_types', 'input_shapes'
        ]).build())

with profile_context.ProfileContext(
    test.get_temp_dir(), trace_steps=[], dump_steps=[]) as pctx:
    with session.Session(
        config=self._no_rewrite_session_config()) as sess, ops.device(dev):
        x = lib.BuildSmallModel()

        self.evaluate(variables.global_variables_initializer())
        pctx.trace_next_step()
        pctx.dump_next_step()
        _ = self.evaluate(x)

        pctx.profiler.profile_name_scope(options=opts)

        with gfile.Open(outfile, 'r') as f:
            # pylint: disable=line-too-long
            dump_str = lib.CheckAndRemoveDoc(f.read())
            outputs = dump_str.split('\n')

            self.assertEqual(
                outputs[0],
                'node name | # parameters | # float_ops | requested bytes | total execution time | accelerator execution time | cpu execution time | assigned devices | op types | op count (run|defined) | input shapes'
            )
            for o in outputs[1:]:
                if o.find('Conv2D ') > 0:
                    metrics = o[o.find('(') + 1:o.find(')')].split(',')
                    # Make sure time is profiled.
                    gap = 1 if test.is_gpu_available() else 2
                    for i in range(3, 6, gap):
                        mat = re.search('(.*)(?:us|ms|sec)/(.*)(?:us|ms|sec)',
                                        metrics[i])
                        self.assertGreater(float(mat.group(1)), 0.0)
                        self.assertGreater(float(mat.group(2)), 0.0)
                    # Make sure device is profiled.
                    if test.is_gpu_available():
                        self.assertTrue(metrics[6].find('gpu') > 0)
                        self.assertFalse(metrics[6].find('cpu') > 0)
                    else:
                        self.assertFalse(metrics[6].find('gpu') > 0)
                        self.assertTrue(metrics[6].find('cpu') > 0)
                    # Make sure float_ops is profiled.
                    mat = re.search('(.*)k/(.*)k flops', metrics[1].strip())
                    self.assertGreater(float(mat.group(1)), 0.0)
                    self.assertGreater(float(mat.group(2)), 0.0)
                    # Make sure op_count is profiled.
                    self.assertEqual(metrics[8].strip(), '1/1|1/1')
                    # Make sure input_shapes is profiled.
                    self.assertEqual(metrics[9].strip(), '0:2x6x6x3|1:3x3x3x6')

                if o.find('DW (3x3x3x6') > 0:
                    metrics = o[o.find('(') + 1:o.find(')')].split(',')
                    mat = re.search('(.*)/(.*) params', metrics[1].strip())
                    self.assertGreater(float(mat.group(1)), 0.0)
                    self.assertGreater(float(mat.group(2)), 0.0)
            # pylint: enable=line-too-long

    # Test that profiler restored from profile file gives the same result.
gfile.Remove(outfile)
profile_file = os.path.join(test.get_temp_dir(), 'profile_1')
with lib.ProfilerFromFile(profile_file) as profiler:
    profiler.profile_name_scope(options=opts)
    with gfile.Open(outfile, 'r') as f:
        self.assertEqual(dump_str, lib.CheckAndRemoveDoc(f.read()))
