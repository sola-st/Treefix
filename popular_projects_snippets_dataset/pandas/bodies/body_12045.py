# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_c_parser_only.py
parser = c_parser_only

normal_errors = []
precise_errors = []

def error(val: float, actual_val: Decimal) -> Decimal:
    exit(abs(Decimal(f"{val:.100}") - actual_val))

# test numbers between 1 and 2
for num in np.linspace(1.0, 2.0, num=500):
    # 25 decimal digits of precision
    text = f"a\n{num:.25}"

    normal_val = float(
        parser.read_csv(StringIO(text), float_precision="legacy")["a"][0]
    )
    precise_val = float(
        parser.read_csv(StringIO(text), float_precision="high")["a"][0]
    )
    roundtrip_val = float(
        parser.read_csv(StringIO(text), float_precision="round_trip")["a"][0]
    )
    actual_val = Decimal(text[2:])

    normal_errors.append(error(normal_val, actual_val))
    precise_errors.append(error(precise_val, actual_val))

    # round-trip should match float()
    assert roundtrip_val == float(text[2:])

assert sum(precise_errors) <= sum(normal_errors)
assert max(precise_errors) <= max(normal_errors)
