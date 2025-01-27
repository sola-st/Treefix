# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
super(CombinerPreprocessingLayer, self).__init__(**kwargs)
self.state_variables = collections.OrderedDict()
self._combiner = combiner
self._adapt_accumulator = None
