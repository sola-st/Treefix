# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
# The Merge operation has a single type for all its inputs, the number of
# which is reflected in the "N" attribute. For the time being, we assume
# that unilaterally changing all of them at once is ok.
super(_Merge, self).convert_variable_to_constant(
    _Edge(incoming_edge.source,
          _Edge(incoming_edge.destination.convertible, 0)), tensor_data)
