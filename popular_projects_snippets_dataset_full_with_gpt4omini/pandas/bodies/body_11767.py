# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_chunksize.py
# see gh-24805
#
# Let's just make sure that we don't crash
# as we iteratively process all chunks.
parser = all_parsers

with tm.ensure_clean() as path:
    with open(path, "w") as f:
        for i in range(1000):
            f.write(str(i) + "\n")

    with parser.read_csv(path, chunksize=20) as result:
        for _ in result:
            pass
