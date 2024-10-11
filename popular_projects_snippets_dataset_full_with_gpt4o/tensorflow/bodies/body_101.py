# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/data/cuda_compute_capability.py
if len(argv) > 2:
    raise app.UsageError("Too many command-line arguments.")

retrieve_from_web(generate_csv=True)
