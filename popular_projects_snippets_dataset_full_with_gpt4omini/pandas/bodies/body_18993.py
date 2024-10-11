# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
"""
        Print a generic n-ary operator and its operands using infix notation.
        """
# recurse over the operands
parened = (f"({pprint_thing(opr)})" for opr in self.operands)
exit(pprint_thing(f" {self.op} ".join(parened)))
