# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Prints the status and info on all configurations in a table format.

  Args:
    configs: List of all configurations found.
    missing: List of all configurations that are missing.
    warning: List of all configurations found with warnings.
  """
print_text = ""
llen = 65  # line length
for i, row in enumerate(configs):
    if i != 0:
        print_text += "-" * llen + "\n"

    if isinstance(row[1], list):
        val = ", ".join(row[1])
    else:
        val = row[1]

    print_text += " {: <28}".format(row[0]) + "    {: <25}".format(val) + "\n"

print_text += "="*llen
print("\n\n {: ^32}    {: ^25}".format("Configuration(s)",
                                       "Detected value(s)"))
print("="*llen)
print(print_text)

if missing:
    print("\n * ERROR: The following configurations are missing:")
    for m in missing:
        print("   ", *m)

if warning:
    print("\n * WARNING: The following configurations could cause issues:")
    for w in warning:
        print("   ", *w)

if not missing and not warning:
    print("\n * INFO: Successfully found all configurations.")

print("\n")
