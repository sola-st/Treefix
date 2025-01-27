# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_strings.py
data = """AAA,BBB,CCC,DDD
0.056674973,8,True,a
2.613230982,2,False,b
3.568935038,7,False,a"""
parser = all_parsers

with pytest.raises(ValueError, match=_msg_validate_usecols_arg):
    parser.read_csv(StringIO(data), usecols=usecols)
