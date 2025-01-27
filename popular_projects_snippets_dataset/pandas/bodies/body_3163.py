# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
# see gh-20353
df = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}, index=["one", "two", "three"])

with tm.ensure_clean() as path:
    # case 1: CRLF as line terminator
    df.to_csv(path, lineterminator="\r\n")
    expected = b",A,B\r\none,1,4\r\ntwo,2,5\r\nthree,3,6\r\n"

    with open(path, mode="rb") as f:
        assert f.read() == expected

with tm.ensure_clean() as path:
    # case 2: LF as line terminator
    df.to_csv(path, lineterminator="\n")
    expected = b",A,B\none,1,4\ntwo,2,5\nthree,3,6\n"

    with open(path, mode="rb") as f:
        assert f.read() == expected

with tm.ensure_clean() as path:
    # case 3: The default line terminator(=os.linesep)(gh-21406)
    df.to_csv(path)
    os_linesep = os.linesep.encode("utf-8")
    expected = (
        b",A,B"
        + os_linesep
        + b"one,1,4"
        + os_linesep
        + b"two,2,5"
        + os_linesep
        + b"three,3,6"
        + os_linesep
    )

    with open(path, mode="rb") as f:
        assert f.read() == expected
