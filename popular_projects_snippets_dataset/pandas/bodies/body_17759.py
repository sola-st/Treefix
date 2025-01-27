# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
b = Timestamp(datetime.now())
base_delta, code = base_delta_code_pair

inc = base_delta * count
index = DatetimeIndex([b + inc * j for j in range(3)])

exp_freq = f"{count:d}{code}" if count > 1 else code
assert frequencies.infer_freq(index) == exp_freq
