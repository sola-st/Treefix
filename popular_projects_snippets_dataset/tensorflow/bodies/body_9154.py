# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
ops.reset_default_graph()
outfile = os.path.join(test.get_temp_dir(), 'dump')
opts = (
    builder(builder.trainable_variables_parameter()).with_file_output(
        outfile).with_accounted_types(['.*']).with_node_names(
            show_name_regexes=['.*model_analyzer_testlib.py.*'
                              ]).account_displayed_op_only(False).select(
                                  ['params', 'float_ops']).build())

with profile_context.ProfileContext(
    test.get_temp_dir(), trace_steps=[], dump_steps=[]) as pctx:
    with session.Session(config=self._no_rewrite_session_config()) as sess:
        x = lib.BuildFullModel()

        self.evaluate(variables.global_variables_initializer())
        pctx.trace_next_step()
        _ = self.evaluate(x)
        tfprof_node = pctx.profiler.profile_python(options=opts)

        # pylint: disable=line-too-long
        with gfile.Open(outfile, 'r') as f:
            lines = f.read().split('\n')
            self.assertGreater(len(lines), 5)
            result = '\n'.join(l[:min(len(l), 80)] for l in lines)
            self.assertTrue(
                compat.as_text(lib.CheckAndRemoveDoc(result)).startswith(
                    'node name | # parameters | # float_ops'))

        self.assertLess(0, tfprof_node.total_exec_micros)
        self.assertEqual(2844, tfprof_node.total_parameters)
        #The graph is modified when MKL is enabled,total_float_ops will
        #be different
        if test_util.IsMklEnabled():
            self.assertLess(101600, tfprof_node.total_float_ops)
        else:
            self.assertLess(145660, tfprof_node.total_float_ops)
        self.assertEqual(8, len(tfprof_node.children))
        self.assertEqual('_TFProfRoot', tfprof_node.name)
        self.assertEqual('model_analyzer_testlib.py:63:BuildFullModel',
                         tfprof_node.children[0].name)
        self.assertEqual(
            'model_analyzer_testlib.py:63:BuildFullModel (gradient)',
            tfprof_node.children[1].name)
        self.assertEqual('model_analyzer_testlib.py:67:BuildFullModel',
                         tfprof_node.children[2].name)
        self.assertEqual(
            'model_analyzer_testlib.py:67:BuildFullModel (gradient)',
            tfprof_node.children[3].name)
        self.assertEqual('model_analyzer_testlib.py:69:BuildFullModel',
                         tfprof_node.children[4].name)
        self.assertEqual('model_analyzer_testlib.py:70:BuildFullModel',
                         tfprof_node.children[5].name)
        self.assertEqual(
            'model_analyzer_testlib.py:70:BuildFullModel (gradient)',
            tfprof_node.children[6].name)
        self.assertEqual('model_analyzer_testlib.py:72:BuildFullModel',
                         tfprof_node.children[7].name)
        # pylint: enable=line-too-long
