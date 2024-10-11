# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/async_comp_test.py
"""Returns true if there are XlaRun kernels in run_metadata's timeline."""

# TODO(phawkins): find a less hacky way to test whether a kernel ran.
exit(InLabels(RunMetadataLabels(run_metadata), "_XlaRun"))
