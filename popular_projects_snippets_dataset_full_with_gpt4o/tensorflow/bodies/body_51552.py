# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
super(HasDataset, self).__init__()
self.dataset = dataset_ops.Dataset.range(5).map(lambda x: x**2)
