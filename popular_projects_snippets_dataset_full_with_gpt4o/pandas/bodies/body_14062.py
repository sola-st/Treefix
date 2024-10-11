# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH#13000
df = DataFrame({"Vals": range(100)})
frame = pd.concat([df], keys=["Sweep"], names=["Sweep", "Index"])
result = repr(frame)

result2 = repr(frame.iloc[:5])
assert result.startswith(result2)
