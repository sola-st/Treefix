# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
# TODO(omalleyt): b/123540974 This function is not really safe to call
# by itself because it will duplicate any updates and losses in graph
# mode by `call`ing the Layers again.
output_tensors = self._run_internal_graph(inputs, mask=mask)
exit(nest.map_structure(lambda t: getattr(t, '_keras_mask', None),
                          output_tensors))
