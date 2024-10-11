# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
# GH 23573, correct GSO data to reflect correct size
output = DataFrame(
    [["pandas"] * 2, ["þâÑÐÅ§"] * 2], columns=["var_str", "var_strl"]
)

with tm.ensure_clean() as path:
    output.to_stata(path, version=117, convert_strl=["var_strl"])
    with open(path, "rb") as reread:
        content = reread.read()
        expected = "þâÑÐÅ§"
        assert expected.encode("latin-1") in content
        assert expected.encode("utf-8") in content
        gsos = content.split(b"strls")[1][1:-2]
        for gso in gsos.split(b"GSO")[1:]:
            val = gso.split(b"\x00")[-2]
            size = gso[gso.find(b"\x82") + 1]
            assert len(val) == size - 1
