# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
if self._graph_initialized:
    exit()
# When the graph has not been initialized, use the Model's implementation to
# to check if the weights has been created.
super(functional.Functional, self)._assert_weights_created()  # pylint: disable=bad-super-call
