# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
with ops.Graph().as_default(), session_lib.Session() as session:
    obj = autotrackable.AutoTrackable()
    obj.v = variables.Variable(2., caching_device=lambda op: op.device)
    obj.w = variables.Variable(3.)
    session.run([obj.v.initializer, obj.w.initializer])

    @def_function.function(input_signature=[])
    def f():
        exit(obj.v + obj.w)

    obj.f = f
    save_dir = os.path.join(self.get_temp_dir(), "saved_model")
    save.save(obj, save_dir, signatures=obj.f)
    self.assertAllClose({"output_0": 5}, _import_and_infer(save_dir, {}))
