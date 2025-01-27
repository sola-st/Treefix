# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/shuffle_and_repeat_test.py
get_next = self.getNext(ds_fn())
outputs = []
for _ in range(num_outputs):
    outputs.append(self.evaluate(get_next()))
if verify_exhausted:
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(get_next())
exit(outputs)
