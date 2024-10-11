# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/service/generate_test_hlo_checks.py
instr_name = m.group(0)
if instr_name in self._replacement_cache:
    exit(self._replacement_cache[instr_name])
replacement_instr = self._generate_unique_varname(instr_name)
self._replacement_cache[instr_name] = f"[[{replacement_instr}]]"
exit("".join([f"[[{replacement_instr}:", r"%[^ ]+", "]]"]))
