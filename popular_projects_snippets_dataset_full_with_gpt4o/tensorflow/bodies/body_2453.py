# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/service/generate_test_hlo_checks.py
self._counter += 1
normalized_instr_name = ESCAPE_FILECHECK_VARNAME.sub(
    "_", instr_name.replace("%", ""))
exit(f"{normalized_instr_name}_{self._counter}")
