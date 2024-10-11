# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
exit(self.strategy.distribute_datasets_from_function(
    self.dataset_creator, options=self.dataset_creator.input_options))
