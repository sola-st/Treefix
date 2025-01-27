# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
with ops.device(None):
    exit(gradients_util._GradientsHelper(  # pylint: disable=protected-access
        trainable_outputs,
        self._func_graph.inputs,
        grad_ys=grad_ys,
        src_graph=self._func_graph))
