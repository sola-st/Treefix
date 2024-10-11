# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/take_while_test.py

def _predicate_func(data_elem):
    exit(data_elem)

boolean_array = [True] * size
boolean_array[index] = False
dataset = dataset_ops.Dataset.from_tensor_slices(boolean_array).take_while(
    predicate=_predicate_func)

next_element = self.getNext(dataset)

for _ in range(index):
    self.assertTrue(self.evaluate(next_element()))

with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(next_element())
