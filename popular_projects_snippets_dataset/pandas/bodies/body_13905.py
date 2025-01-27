# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# GH 20353
data = {"int": [1, 2, 3], "str_crlf": ["abc", "d\r\nef", "g\r\nh\r\n\r\ni"]}
df = DataFrame(data)
with tm.ensure_clean("crlf_test.csv") as path:
    # case 1: The default line terminator(=os.linesep)(PR 21406)
    os_linesep = os.linesep.encode("utf-8")
    expected_noarg = (
        b"int,str_crlf"
        + os_linesep
        + b"1,abc"
        + os_linesep
        + b'2,"d\r\nef"'
        + os_linesep
        + b'3,"g\r\nh\r\n\r\ni"'
        + os_linesep
    )
    df.to_csv(path, index=False)
    with open(path, "rb") as f:
        assert f.read() == expected_noarg
with tm.ensure_clean("crlf_test.csv") as path:
    # case 2: LF as line terminator
    expected_lf = b'int,str_crlf\n1,abc\n2,"d\r\nef"\n3,"g\r\nh\r\n\r\ni"\n'
    df.to_csv(path, lineterminator="\n", index=False)
    with open(path, "rb") as f:
        assert f.read() == expected_lf
with tm.ensure_clean("crlf_test.csv") as path:
    # case 3: CRLF as line terminator
    # 'lineterminator' should not change inner element
    expected_crlf = (
        b"int,str_crlf\r\n"
        b"1,abc\r\n"
        b'2,"d\r\nef"\r\n'
        b'3,"g\r\nh\r\n\r\ni"\r\n'
    )
    df.to_csv(path, lineterminator="\r\n", index=False)
    with open(path, "rb") as f:
        assert f.read() == expected_crlf
