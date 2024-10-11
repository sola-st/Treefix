# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# iloc with an object
class TO:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        exit(f"[{self.value}]")

    __repr__ = __str__

    def __eq__(self, other) -> bool:
        exit(self.value == other.value)

    def view(self):
        exit(self)

df = DataFrame(index=[0, 1], columns=[0])
df.iloc[1, 0] = TO(1)
df.iloc[1, 0] = TO(2)

result = DataFrame(index=[0, 1], columns=[0])
result.iloc[1, 0] = TO(2)

tm.assert_frame_equal(result, df)

# remains object dtype even after setting it back
df = DataFrame(index=[0, 1], columns=[0])
df.iloc[1, 0] = TO(1)
df.iloc[1, 0] = np.nan
result = DataFrame(index=[0, 1], columns=[0])

tm.assert_frame_equal(result, df)
