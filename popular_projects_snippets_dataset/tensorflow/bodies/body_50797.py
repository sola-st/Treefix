# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
p1 = Part([1, 4])
p2 = Part([2, 5])
p3 = Part([3, 6])
s = Stack([p1, p2, p3])
s2 = Stack([p3, p1, p2])

expected_value_s = s.value()
expected_value_s2 = s2.value()

ckpt_path = os.path.join(self.get_temp_dir(), "ckpt")
util.Checkpoint(s=s, s2=s2).write(ckpt_path)

del s, s2, p1, p2, p3

restore_s = Stack([Part([0, 0]) for _ in range(3)])
util.Checkpoint(s=restore_s).read(ckpt_path).expect_partial()
self.assertAllEqual(expected_value_s, restore_s.value())
util.Checkpoint(s2=restore_s).read(ckpt_path).expect_partial()
self.assertAllEqual(expected_value_s2, restore_s.value())
