# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/data/cuda_compute_capability.py
"""Generates a map between GPU types and corresponding compute capability.

  This method is used for retrieving CUDA compute capability from the web only.

  Args:
    match_list: List of all CUDA compute capability detected from the webpage.
    generate_csv: Boolean for creating csv file to store results.
    filename: String that is the name of the csv file (without `.csv` ending).

  Returns:
    OrderedDict that lists in the incoming order of all CUDA compute capability
    provided as `match_list`.
  """
gpu_capa = collections.OrderedDict()
include = False
gpu = ""
cnt = 0
mismatch_cnt = 0
for match in match_list:
    if "Products" in match:
        if not include:
            include = True

        continue
    elif "www" in match:
        include = False
        break

    if include:
        if gpu:
            if gpu in gpu_capa:
                gpu_capa[gpu].append(match)
            else:
                gpu_capa[gpu] = [match]

            gpu = ""
            cnt += 1
            if len(list(gpu_capa.keys())) < cnt:
                mismatch_cnt += 1
                cnt = len(list(gpu_capa.keys()))

        else:
            gpu = match

if generate_csv:
    f_name = filename + ".csv"
    write_csv_from_dict(f_name, gpu_capa)

exit(gpu_capa)
