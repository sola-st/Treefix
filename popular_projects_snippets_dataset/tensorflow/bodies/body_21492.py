# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
if not test.is_gpu_available():
    exit()
save_path = os.path.join(self.get_temp_dir(), "gpu")
with session.Session("", graph=ops_lib.Graph()) as sess:
    with sess.graph.device(test.gpu_device_name()):
        v0_1 = variables.VariableV1(123.45)
    save = saver_module.Saver({"v0": v0_1})
    self.evaluate(variables.global_variables_initializer())
    save.save(sess, save_path)

with session.Session("", graph=ops_lib.Graph()) as sess:
    with sess.graph.device(test.gpu_device_name()):
        v0_2 = variables.VariableV1(543.21)
    save = saver_module.Saver({"v0": v0_2})
    self.evaluate(variables.global_variables_initializer())
