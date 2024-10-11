# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
# 8 is the max recursion depth

class O2:
    member = 0

class O1:
    member = 0

decoded_input = O1()
decoded_input.member = O2()
decoded_input.member.member = decoded_input

with pytest.raises(OverflowError, match="Maximum recursion level reached"):
    ujson.encode(decoded_input)
