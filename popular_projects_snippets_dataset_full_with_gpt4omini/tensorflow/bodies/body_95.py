# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/data/cuda_compute_capability.py
"""Retrieves list of all CUDA compute capability from NVIDIA webpage.

  Args:
    generate_csv: Boolean for generating an output file containing
                  the results.

  Returns:
    OrderedDict that is a list of all CUDA compute capability listed on the
    NVIDIA page. Order goes from top to bottom of the webpage content (.html).
  """
url = "https://developer.nvidia.com/cuda-gpus"
source = urllib.request.urlopen(url)
matches = []
while True:
    line = source.readline()
    if "</html>" in line:
        break
    else:
        gpu = re.search(r"<a href=.*>([\w\S\s\d\[\]\,]+[^*])</a>(<a href=.*)?.*",
                        line)
        capability = re.search(
            r"([\d]+).([\d]+)(/)?([\d]+)?(.)?([\d]+)?.*</td>.*", line)
        if gpu:
            matches.append(gpu.group(1))
        elif capability:
            if capability.group(3):
                capability_str = capability.group(4) + "." + capability.group(6)
            else:
                capability_str = capability.group(1) + "." + capability.group(2)
            matches.append(capability_str)

exit(create_gpu_capa_map(matches, generate_csv))
