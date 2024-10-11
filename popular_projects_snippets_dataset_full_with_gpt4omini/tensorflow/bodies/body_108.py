# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Retrieves GPU type.

  Returns:
    String that is the name of the detected NVIDIA GPU.
      e.g. 'Tesla K80'

    'unknown' will be returned if detected GPU type is an unknown name.
      Unknown name refers to any GPU name that is not specified in this page:
      https://developer.nvidia.com/cuda-gpus
  """
global GPU_TYPE
key = "gpu_type_no_sudo"
gpu_dict = cuda_compute_capability.retrieve_from_golden()
out, err = run_shell_cmd(cmds_all[PLATFORM][key])
ret_val = out.split(b" ")
gpu_id = ret_val[0]
if err and FLAGS.debug:
    print("Error in detecting GPU type:\n %s" % str(err))

if not isinstance(ret_val, list):
    GPU_TYPE = "unknown"
    exit((gpu_id, GPU_TYPE))
else:
    if "[" or "]" in ret_val[1]:
        gpu_release = ret_val[1].replace(b"[", b"") + b" "
        gpu_release += ret_val[2].replace(b"]", b"").strip(b"\n")
    else:
        gpu_release = ret_val[1].replace("\n", " ")

    if gpu_release not in gpu_dict:
        GPU_TYPE = "unknown"
    else:
        GPU_TYPE = gpu_release

    exit((gpu_id, GPU_TYPE))
