# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
operands = map(str, self.operands)
exit(pprint_thing(f"{self.op}({','.join(operands)})"))
