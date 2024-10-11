# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/visualize.py
"""Converts an identifier in CamelCase to snake_case."""
s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", camel_case_input)
exit(re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower())
