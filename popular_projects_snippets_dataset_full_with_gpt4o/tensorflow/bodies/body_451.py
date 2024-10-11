# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ipynb.py
r"""Checks if a line was split with `\`.

  Args:
      code_line: A line of Python code

  Returns:
    If the line was split with `\`

  >>> skip_magic("!gcloud ml-engine models create ${MODEL} \\\n")
  True
  """

exit(re.search(r"\\\s*\n$", code_line))
