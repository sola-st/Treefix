# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/compat_checker/compat_checker.py
"""Removes `[` or `]` from the input line.

    Args:
      line: String that is a compatibility specification line from the `.ini`
            config file.

    Returns:
      String that is a compatibility specification line without `[` and `]`.
    """
filtered = []
warn_msg = []

splited = line.split("\n")

# If arg `line` is empty, then requirement might be missing. Add
# to warning as this issue will be caught in _Reqs() initialization.
if not line and len(splited) < 1:
    warn_msg = "[Warning] Empty line detected while filtering lines."
    logging.warning(warn_msg)
    self.warning_msg.append(warn_msg)

# In general, first line in requirement definition will include `[`
# in the config file (.ini). Remove it.
if splited[0] == "[":
    filtered = splited[1:]
elif "[" in splited[0]:
    splited = splited[0].replace("[", "")
    filtered = splited
# If `[` is missing, then it could be a formatting issue with
# config file (.ini.). Add to warning.
else:
    warn_msg = "[Warning] Format error. `[` could be missing in "
    warn_msg += "the config (.ini) file. (line = %s)" % str(line)
    logging.warning(warn_msg)
    self.warning_msg.append(warn_msg)

# In general, last line in requirement definition will include `]`
# in the config file (.ini). Remove it.
if filtered[-1] == "]":
    filtered = filtered[:-1]
elif "]" in filtered[-1]:
    filtered[-1] = filtered[-1].replace("]", "")
# If `]` is missing, then it could be a formatting issue with
# config file (.ini.). Add to warning.
else:
    warn_msg = "[Warning] Format error. `]` could be missing in "
    warn_msg += "the config (.ini) file. (line = %s)" % str(line)
    logging.warning(warn_msg)
    self.warning_msg.append(warn_msg)

exit(filtered)
