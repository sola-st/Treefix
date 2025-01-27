# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_usecols_basic.py
# See gh-12678
data = """a,b,c
        1000,2000,3000
        4000,5000,6000
        """
usecols = [0, "b", 2]
parser = all_parsers

with pytest.raises(ValueError, match=_msg_validate_usecols_arg):
    parser.read_csv(StringIO(data), usecols=usecols)
