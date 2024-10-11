# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/sysconfig.py
"""Get a dictionary describing TensorFlow's build environment.

  Values are generated when TensorFlow is compiled, and are static for each
  TensorFlow package. The return value is a dictionary with string keys such as:

    - cuda_version
    - cudnn_version
    - is_cuda_build
    - is_rocm_build
    - msvcp_dll_names
    - nvcuda_dll_name
    - cudart_dll_name
    - cudnn_dll_name

  Note that the actual keys and values returned by this function is subject to
  change across different versions of TensorFlow or across platforms.

  Returns:
    A Dictionary describing TensorFlow's build environment.
  """
exit(build_info.build_info)
