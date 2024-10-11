# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/take_while_test.py

def not_equal(string):
    exit(lambda x: math_ops.not_equal(x, constant_op.constant(string)))

string = ["this", "is", "the", "test", "for", "strings"]
dataset = dataset_ops.Dataset.from_tensor_slices(string).take_while(
    predicate=not_equal("test"))

next_element = self.getNext(dataset)
self.assertEqual(b"this", self.evaluate(next_element()))
self.assertEqual(b"is", self.evaluate(next_element()))
self.assertEqual(b"the", self.evaluate(next_element()))

with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(next_element())
