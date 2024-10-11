# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/choose_from_datasets_test.py
words = [b"foo", b"bar", b"baz"]
datasets = [dataset_ops.Dataset.from_tensors(w).repeat() for w in words]
choice_array = np.random.randint(3, size=(15,), dtype=np.int64)
choice_dataset = dataset_ops.Dataset.from_tensor_slices(choice_array)
dataset = dataset_ops.Dataset.choose_from_datasets(datasets, choice_dataset)
next_element = self.getNext(dataset)
for i in choice_array:
    self.assertEqual(words[i], self.evaluate(next_element()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(next_element())
