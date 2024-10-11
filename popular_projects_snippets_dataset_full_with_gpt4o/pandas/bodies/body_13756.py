# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
exp_l1_c0 = {"is_visible": True, "attributes": "", "display_value": "c1_a"}
exp_l1_c1 = {"is_visible": True, "attributes": "", "display_value": "c1_b"}

ctx = mi_styler._translate(True, sparse_columns)

assert exp_cols[0].items() <= ctx["head"][0][2].items()
assert exp_cols[1].items() <= ctx["head"][0][3].items()
assert exp_l1_c0.items() <= ctx["head"][1][2].items()
assert exp_l1_c1.items() <= ctx["head"][1][3].items()
