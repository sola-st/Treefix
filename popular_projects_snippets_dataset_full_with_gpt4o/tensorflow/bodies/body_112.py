# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Retrieves CUDA compute capability based on the detected GPU type.

  This function uses the `cuda_compute_capability` module to retrieve the
  corresponding CUDA compute capability for the given GPU type.

  Args:
    source_from_url: Boolean deciding whether to source compute capability
                     from NVIDIA website or from a local golden file.

  Returns:
    List of all supported CUDA compute capabilities for the given GPU type.
      e.g. ['3.5', '3.7']
  """
if not GPU_TYPE:
    if FLAGS.debug:
        print("Warning: GPU_TYPE is empty. "
              "Make sure to call `get_gpu_type()` first.")

elif GPU_TYPE == "unknown":
    if FLAGS.debug:
        print("Warning: Unknown GPU is detected. "
              "Skipping CUDA compute capability retrieval.")

else:
    if source_from_url:
        cuda_compute_capa = cuda_compute_capability.retrieve_from_web()
    else:
        cuda_compute_capa = cuda_compute_capability.retrieve_from_golden()

    exit(cuda_compute_capa[GPU_TYPE])
exit()
