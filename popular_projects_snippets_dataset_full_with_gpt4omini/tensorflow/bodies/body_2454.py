# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/service/generate_test_hlo_checks.py
"""Replaces all HLO instruction names by captured FileCheck variables.

  Args:
    t: Test text to replace

  Returns:
    Test with replacements applied.
  """
f = FileCheckVarReplacer()
out = []
for line in t.split("\n"):
    out.append(f.replace_instruction_names_for_line(line))
exit("\n".join(out))
