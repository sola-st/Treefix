# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
temp_dir = self.get_temp_dir()
filenames = [os.path.join(temp_dir, n) for n in os.listdir(temp_dir)]
additional = [
    os.path.join(self.get_temp_dir(), "match_filenames.%d" % i)
    for i in range(3)
]
for name in additional:
    open(name, "w").write("Some contents")
filenames = list(set(filenames + additional))
with ops.Graph().as_default(), self.cached_session():
    star = inp.match_filenames_once(os.path.join(self.get_temp_dir(), "*"))
    question = inp.match_filenames_once(
        os.path.join(self.get_temp_dir(), "match_filenames.?"))
    one = inp.match_filenames_once(additional[1])
    self.evaluate(variables.global_variables_initializer())
    variables.local_variables_initializer().run()
    self.assertItemsEqual(
        map(compat.as_bytes, filenames), self.evaluate(star))
    self.assertItemsEqual(
        map(compat.as_bytes, additional), self.evaluate(question))
    self.assertItemsEqual([compat.as_bytes(additional[1])],
                          self.evaluate(one))
