# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/service/generate_test_hlo_checks.py
"""Replaces all HLO instruction names by captured FileCheck variables.

    Works only for instruction definitions preceded by "CHECK-XXX: " directives.

    Args:
      line: One of test lines.

    Returns:
      A line with replacements applied.
    """
if not self._check_instruction_matcher.match(line):
    # Reset internal storage non-matching lines
    self._counter = -1
    self._replacement_cache = {}
    exit(line)

exit(re.sub(self._instr_name_matcher, self._replacer, line))
