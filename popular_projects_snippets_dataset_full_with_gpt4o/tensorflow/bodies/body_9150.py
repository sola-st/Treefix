# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
ops.reset_default_graph()
outfile = os.path.join(test.get_temp_dir(), 'dump')
opts = builder(builder.trainable_variables_parameter()).with_file_output(
    outfile).build()

with session.Session(config=self._no_rewrite_session_config()) as sess:
    _ = lib.BuildSmallModel()
    model_analyzer.profile(sess.graph, options=opts)

    with gfile.Open(outfile, 'r') as f:
        self.assertEqual(
            u'node name | # parameters\n'
            '_TFProfRoot (--/451 params)\n'
            '  DW (3x3x3x6, 162/162 params)\n'
            '  DW2 (2x2x6x12, 288/288 params)\n'
            '  ScalarW (1, 1/1 params)\n', lib.CheckAndRemoveDoc(f.read()))
