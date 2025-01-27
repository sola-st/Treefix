# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
all_inputs = []
dataset = dataset_ops.Dataset.from_tensors(1.).repeat()
dist.extended.experimental_run_steps_on_iterator(
    lambda _, inputs: all_inputs.append(self.evaluate(inputs)),
    dataset_ops.make_one_shot_iterator(dataset))
self.assertEqual(all_inputs, [1.])
