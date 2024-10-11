# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_info.py
buf = StringIO()
size = 1001
start = 5
frame = DataFrame(np.random.randn(3, size))
frame.info(verbose=True, buf=buf)

res = buf.getvalue()
header = " #     Column  Dtype  \n---    ------  -----  "
assert header in res

frame.info(verbose=True, buf=buf)
buf.seek(0)
lines = buf.readlines()
assert len(lines) > 0

for i, line in enumerate(lines):
    if start <= i < start + size:
        line_nr = f" {i - start} "
        assert line.startswith(line_nr)
