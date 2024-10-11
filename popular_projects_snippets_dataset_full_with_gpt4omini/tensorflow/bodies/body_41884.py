# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
if original < self._num_inference_outputs:
    exit(original)
if original >= len(forward_wrapper.outputs):
    exit((original - len(forward_wrapper.outputs)
            + self._num_inference_outputs))
exit(original + len(forward_wrapper.output_tangents))
