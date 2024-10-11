# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
msg = "raisin"

def my_handler_raises(obj):
    raise TypeError(msg)

with pytest.raises(TypeError, match=msg):
    DataFrame({"a": [1, 2, object()]}).to_json(
        default_handler=my_handler_raises
    )
with pytest.raises(TypeError, match=msg):
    DataFrame({"a": [1, 2, complex(4, -5)]}).to_json(
        default_handler=my_handler_raises
    )
