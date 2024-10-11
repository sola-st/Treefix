# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
if self._intra_op_parallelism_threads == num_threads:
    exit()

if self._context_handle is not None:
    raise RuntimeError(
        "Intra op parallelism cannot be modified after initialization.")

self._intra_op_parallelism_threads = num_threads
