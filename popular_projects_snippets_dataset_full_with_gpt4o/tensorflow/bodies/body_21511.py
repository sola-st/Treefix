# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
# train.Saver is V1 only API.
with ops_lib.Graph().as_default(), self.cached_session():
    v0 = variables.VariableV1(123, name="v0")
    save = saver_module.Saver({"v0": v0}, sharded=True)
    sd = save.as_saver_def()
    self.assertTrue(sd.sharded)
