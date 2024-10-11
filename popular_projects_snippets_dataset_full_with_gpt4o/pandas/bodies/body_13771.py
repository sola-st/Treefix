# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# GH 41893
func = {
    "apply": lambda s: ["attr: val;" if "b" in v else "" for v in s],
    "applymap": lambda v: "attr: val" if "b" in v else "",
}
result = getattr(mi_styler, f"{method}_index")(func[method], axis=axis)._compute()
expected = {(1, 1): [("attr", "val")]}
assert getattr(result, f"ctx_{axis}") == expected
