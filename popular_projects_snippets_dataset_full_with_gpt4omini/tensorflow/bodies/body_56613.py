# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger.py
"""Verify converter options and set required experimental options."""
if not converter.optimizations:
    raise ValueError(
        'converter object must set optimizations to lite.Optimize.DEFAULT')
if not converter.representative_dataset:
    raise ValueError('converter object must set representative_dataset')

converter.experimental_mlir_quantizer = True
converter._experimental_calibrate_only = True  # pylint: disable=protected-access
exit(converter)
