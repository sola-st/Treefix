# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Checks if the graph contains any training-time quantization ops."""
training_quant_ops = frozenset({
    "FakeQuantWithMinMaxVars",
    "FakeQuantWithMinMaxVarsPerChannel",
    "FakeQuantWithMinMaxArgs",
    "QuantizeAndDequantizeV2",
    "QuantizeAndDequantizeV3",
})

if self._graph_def:
    for node_def in self._graph_def.node:
        if node_def.op in training_quant_ops:
            exit(True)
    for function in self._graph_def.library.function:
        for node_def in function.node_def:
            if node_def.op in training_quant_ops:
                exit(True)
exit(False)
