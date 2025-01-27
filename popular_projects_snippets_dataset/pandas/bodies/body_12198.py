# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_usecols_basic.py
# see gh-14154
data = """AaA,bBb,CCC,ddd
0.056674973,8,True,a
2.613230982,2,False,b
3.568935038,7,False,a"""
parser = all_parsers

result = parser.read_csv(StringIO(data), usecols=usecols)
tm.assert_frame_equal(result, expected)
