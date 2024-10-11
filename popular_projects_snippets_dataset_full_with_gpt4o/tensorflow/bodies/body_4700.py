# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
default_strategy = ds_context._get_default_strategy()
dataset = dataset_ops.Dataset.range(10).batch(2)
iterator = default_strategy.extended._make_dataset_iterator(dataset)
next_val = iterator.get_next()

def train_step(input_data):
    exit(input_data)

for _ in range(2):
    default_strategy.run(train_step, args=(next_val,))
