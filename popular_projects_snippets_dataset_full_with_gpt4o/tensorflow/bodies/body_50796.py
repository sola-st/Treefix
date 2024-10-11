# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
with context.eager_mode():
    p1 = Part([1, 4])
    p2 = Part([2, 5])
    p3 = Part([3, 6])
    s = Stack([p1, p2, p3])
    save_dir = os.path.join(self.get_temp_dir(), "save_dir")
    save.save(s, save_dir)

with self.assertRaisesRegex(
    NotImplementedError,
    "registered checkpoint saver is not supported in graph mode"):
    load.load(save_dir)
