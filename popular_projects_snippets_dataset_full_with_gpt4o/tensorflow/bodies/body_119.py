# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Runs all functions for detecting user machine configurations.

  Returns:
    Tuple
      (List of all configurations found,
       List of all missing configurations,
       List of all configurations found with warnings,
       Dict of all configurations)
  """
all_functions = collections.OrderedDict(
    [("Platform", get_platform()),
     ("CPU", get_cpu_type()),
     ("CPU arch", get_cpu_arch()),
     ("Distribution", get_distrib()),
     ("Distribution version", get_distrib_version()),
     ("GPU", get_gpu_type()[1]),
     ("GPU count", get_gpu_count()),
     ("CUDA version (default)", get_cuda_version_default()),
     ("CUDA versions (all)", get_cuda_version_all()),
     ("CUDA compute capability",
      get_cuda_compute_capability(get_gpu_type()[1])),
     ("cuDNN version", get_cudnn_version()),
     ("GCC version", get_gcc_version()),
     ("Python version (default)", get_python_version()),
     ("GNU C Lib (glibc) version", get_glibc_version()),
     ("libstdc++ version", get_libstdcpp_version()),
     ("CPU ISA (min requirement)", get_cpu_isa_version())]
)
configs_found = []
json_data = {}
missing = []
warning = []
for config, call_func in all_functions.items():
    ret_val = call_func
    if not ret_val:
        configs_found.append([config, "\033[91m\033[1mMissing\033[0m"])
        missing.append([config])
        json_data[config] = ""
    elif ret_val == "unknown":
        configs_found.append([config, "\033[93m\033[1mUnknown type\033[0m"])
        warning.append([config, ret_val])
        json_data[config] = "unknown"

    else:
        if "ISA" in config:
            if not ret_val[1]:
                # Not missing any required ISA
                configs_found.append([config, ret_val[0]])
                json_data[config] = ret_val[0]
            else:
                configs_found.append([
                    config,
                    "\033[91m\033[1mMissing " + str(ret_val[1][1:-1]) + "\033[0m"
                ])
                missing.append(
                    [config,
                     "\n\t=> Found %s but missing %s"
                     % (str(ret_val[0]), str(ret_val[1]))]
                )
                json_data[config] = ret_val[0]

        else:
            configs_found.append([config, ret_val])
            json_data[config] = ret_val

exit((configs_found, missing, warning, json_data))
