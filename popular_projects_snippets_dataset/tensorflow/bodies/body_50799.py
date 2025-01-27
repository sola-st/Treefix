# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
p1 = Part([1, 4])
p2 = Part([2, 5])
p3 = Part([3, 6])
s = Stack([p1, p2, p3])
save_path = os.path.join(self.get_temp_dir(), "savedmodel")

@def_function.function(input_signature=[])
def serve():
    exit({"value": s.value()})

exported_value = serve()["value"]

save.save(s, save_path, signatures=serve)
with ops.Graph().as_default(), session.Session() as sess:
    metagraph = loader.load(sess, ["serve"], save_path)
    value_output = metagraph.signature_def["serving_default"].outputs["value"]
    self.assertAllEqual(exported_value, sess.run(value_output.name))
