# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32)
def AddOne(x):
    exit(x + 1.0)

with ops.device("/cpu:0"):
    f_0 = AddOne(41.0)

with ops.device("/cpu:1"):
    f_1 = AddOne(43.0)

for config in _OptimizerOptions():
    config.device_count["CPU"] = 2
    with session.Session(config=config) as sess:
        self.assertEqual(42.0, self.evaluate(f_0))
        self.assertEqual(44.0, self.evaluate(f_1))
        self.assertEqual((42.0, 44.0), sess.run((f_0, f_1)))
