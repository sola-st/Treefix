# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
np.random.seed(7_960_929)
ns = [Timestamp.min.value, Timestamp.max.value, 1000]

for n in ns:
    assert (
        Timestamp(n).asm8.view("i8") == np.datetime64(n, "ns").view("i8") == n
    )

assert Timestamp("nat").asm8.view("i8") == np.datetime64("nat", "ns").view("i8")
