# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
orders = []
for _ in range(num_rounds):
    orders.append(self.getDatasetOutput(dataset))
exit(orders)
