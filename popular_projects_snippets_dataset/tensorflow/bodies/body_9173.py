# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profile_context_test.py
ops.reset_default_graph()
x = lib.BuildFullModel()

with profile_context.ProfileContext(test.get_temp_dir(), debug=True):
    with session.Session() as sess:
        self.evaluate(variables.global_variables_initializer())
        for _ in range(10):
            self.evaluate(x)
            for f in gfile.ListDirectory(test.get_temp_dir()):
                # Warm up, no tracing.
                self.assertFalse("run_meta" in f)
        self.evaluate(x)
        self.assertTrue(
            gfile.Exists(os.path.join(test.get_temp_dir(), "run_meta_11")))
        gfile.Remove(os.path.join(test.get_temp_dir(), "run_meta_11"))
        # fetched already.
        self.evaluate(x)
        for f in gfile.ListDirectory(test.get_temp_dir()):
            self.assertFalse("run_meta" in f)
