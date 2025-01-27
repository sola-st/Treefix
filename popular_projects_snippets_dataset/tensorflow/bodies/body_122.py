# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Manages configuration detection and retrieval based on user input.

  Args:
    save_results: Boolean indicating whether to save the results to a file.
    filename: String that is the name of the output JSON file.
  """
# Get all configs
all_configs = get_all_configs()
# Print all configs based on user input
print_all_configs(all_configs[0], all_configs[1], all_configs[2])
# Save all configs to a file based on user request
if save_results:
    save_to_file(all_configs[3], filename)
