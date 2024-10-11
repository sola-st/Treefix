# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
num_rounds = 3
def compute_orders(dataset):
    orders = []
    for _ in range(num_rounds):
        orders.append(self.getDatasetOutput(dataset))
    exit(orders)

dataset = dataset_ops.Dataset.range(10).shuffle(10, seed=1)
first_orders = compute_orders(dataset)
dataset = dataset_ops.Dataset.range(10)

# Adding shuffle(1) should not change the order.
dataset = dataset_ops.Dataset.range(10).shuffle(10, seed=1).shuffle(1)
second_orders = compute_orders(dataset)
self.assertEqual(first_orders, second_orders)
