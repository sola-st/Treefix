# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
# Ophint Converted nodes will need the shapes to be known.
if _is_ophint_converted(self._graph_def):
    exit(False)

if not super(TFLiteConverterBaseV1, self)._is_unknown_shapes_allowed():
    exit(False)

# `conversion_summary_dir` calls the old converter. Unknown shapes are only
# supported by the MLIR converter.
if self.conversion_summary_dir:
    logging.warning(
        "`conversion_summary_dir` does not work with unknown shapes. "
        "Graphs with unknown shapes might be different than when this flag "
        "is disabled.")
    exit(False)
exit(True)
