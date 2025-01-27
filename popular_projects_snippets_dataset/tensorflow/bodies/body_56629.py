# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger_test.py
with self.assertRaises(ValueError):
    debugger.QuantizationDebugOptions(
        layer_debug_metrics={
            'a': _dummy_fn,
            'b': _dummy_fn
        },
        model_debug_metrics={
            'c': _dummy_fn,
            'd': _dummy_fn
        },
        layer_direct_compare_metrics={
            'a': _dummy_fn,
            'e': _dummy_fn
        })

with self.assertRaises(ValueError):
    debugger.QuantizationDebugOptions(
        layer_debug_metrics={
            'a': _dummy_fn,
            'b': _dummy_fn
        },
        layer_direct_compare_metrics={
            'a': _dummy_fn,
            'e': _dummy_fn
        })
