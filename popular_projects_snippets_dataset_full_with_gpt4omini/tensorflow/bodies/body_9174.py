# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profile_context_test.py
ops.reset_default_graph()
x = lib.BuildFullModel()
with profile_context.ProfileContext(
    test.get_temp_dir(), enabled=False) as pctx:
    with session.Session() as sess:
        self.evaluate(variables.global_variables_initializer())
        for _ in range(10):
            self.evaluate(x)
    self.assertTrue(pctx.profiler is None)
    self.assertTrue(
        getattr(session.BaseSession, "profile_context", None) is None)

with profile_context.ProfileContext(test.get_temp_dir()) as pctx:
    with session.Session() as sess:
        self.evaluate(variables.global_variables_initializer())
        for _ in range(10):
            self.evaluate(x)
    self.assertFalse(pctx.profiler is None)
    self.assertFalse(
        getattr(session.BaseSession, "profile_context", None) is None)
