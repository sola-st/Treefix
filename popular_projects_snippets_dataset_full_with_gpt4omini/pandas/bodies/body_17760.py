# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
b = Timestamp(datetime.now())
base_delta, _ = base_delta_code_pair

index = constructor(b, base_delta)
assert frequencies.infer_freq(index) is None
