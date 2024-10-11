# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/saved_model_test.py
# simulate a training process to mutate the state of the model.
self.v1.assign([2, 2, 2, 2])
self.v2.assign([3, 3, 3, 3])
self.table.insert(keys=1, values=1)
