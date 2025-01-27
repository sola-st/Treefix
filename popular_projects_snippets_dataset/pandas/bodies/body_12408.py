# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
if writer_name in ["to_latex"]:  # uses Styler implementation
    pytest.importorskip("jinja2")
p1 = tm.ensure_clean("string")
p2 = tm.ensure_clean("fspath")
df = pd.DataFrame({"A": [1, 2]})

with p1 as string, p2 as fspath:
    pytest.importorskip(module)
    mypath = CustomFSPath(fspath)
    writer = getattr(df, writer_name)

    writer(string, **writer_kwargs)
    writer(mypath, **writer_kwargs)
    with open(string, "rb") as f_str, open(fspath, "rb") as f_path:
        if writer_name == "to_excel":
            # binary representation of excel contains time creation
            # data that causes flaky CI failures
            result = pd.read_excel(f_str, **writer_kwargs)
            expected = pd.read_excel(f_path, **writer_kwargs)
            tm.assert_frame_equal(result, expected)
        else:
            result = f_str.read()
            expected = f_path.read()
            assert result == expected
