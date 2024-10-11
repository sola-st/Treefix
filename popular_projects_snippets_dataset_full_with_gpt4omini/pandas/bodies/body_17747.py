# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
freq = freq.upper()

gen = date_range("1/1/2000", periods=periods, freq=freq)
index = DatetimeIndex(gen.values)

if not freq.startswith("Q-"):
    assert frequencies.infer_freq(index) == gen.freqstr
else:
    inf_freq = frequencies.infer_freq(index)
    is_dec_range = inf_freq == "Q-DEC" and gen.freqstr in (
        "Q",
        "Q-DEC",
        "Q-SEP",
        "Q-JUN",
        "Q-MAR",
    )
    is_nov_range = inf_freq == "Q-NOV" and gen.freqstr in (
        "Q-NOV",
        "Q-AUG",
        "Q-MAY",
        "Q-FEB",
    )
    is_oct_range = inf_freq == "Q-OCT" and gen.freqstr in (
        "Q-OCT",
        "Q-JUL",
        "Q-APR",
        "Q-JAN",
    )
    assert is_dec_range or is_nov_range or is_oct_range
