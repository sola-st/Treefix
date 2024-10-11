# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profile_context_test.py
ops.reset_default_graph()
outfile = os.path.join(test.get_temp_dir(), "dump")
opts = builder(builder.time_and_memory()).with_file_output(outfile).build()

x = lib.BuildFullModel()

profile_str = None
profile_step100 = os.path.join(test.get_temp_dir(), "profile_100")
with profile_context.ProfileContext(test.get_temp_dir()) as pctx:
    pctx.add_auto_profiling("op", options=opts, profile_steps=[15, 50, 100])
    with session.Session() as sess:
        self.evaluate(variables.global_variables_initializer())
        total_steps = 101
        for i in range(total_steps):
            self.evaluate(x)
            if i == 14 or i == 49:
                self.assertTrue(gfile.Exists(outfile))
                gfile.Remove(outfile)
            if i == 99:
                self.assertTrue(gfile.Exists(profile_step100))
                with gfile.Open(outfile, "r") as f:
                    profile_str = f.read()
                gfile.Remove(outfile)

    self.assertEqual(set([15, 50, 100]), set(pctx.get_profiles("op").keys()))

with lib.ProfilerFromFile(os.path.join(test.get_temp_dir(),
                                       "profile_100")) as profiler:
    profiler.profile_operations(options=opts)
    with gfile.Open(outfile, "r") as f:
        self.assertEqual(profile_str, f.read())
