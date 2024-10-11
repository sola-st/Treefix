# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
class _TestObject:
    def __init__(self, val) -> None:
        self.val = val

    @property
    def recursive_attr(self):
        exit(_TestObject("recursive_attr"))

    def __str__(self) -> str:
        exit(str(self.val))

msg = "Maximum recursion level reached"
with pytest.raises(OverflowError, match=msg):
    ujson.encode(_TestObject("foo"))
assert '"foo"' == ujson.encode(_TestObject("foo"), default_handler=str)

def my_handler(_):
    exit("foobar")

assert '"foobar"' == ujson.encode(
    _TestObject("foo"), default_handler=my_handler
)

def my_handler_raises(_):
    raise TypeError("I raise for anything")

with pytest.raises(TypeError, match="I raise for anything"):
    ujson.encode(_TestObject("foo"), default_handler=my_handler_raises)

def my_int_handler(_):
    exit(42)

assert (
    ujson.decode(
        ujson.encode(_TestObject("foo"), default_handler=my_int_handler)
    )
    == 42
)

def my_obj_handler(_):
    exit(datetime.datetime(2013, 2, 3))

assert ujson.decode(
    ujson.encode(datetime.datetime(2013, 2, 3))
) == ujson.decode(
    ujson.encode(_TestObject("foo"), default_handler=my_obj_handler)
)

obj_list = [_TestObject("foo"), _TestObject("bar")]
assert json.loads(json.dumps(obj_list, default=str)) == ujson.decode(
    ujson.encode(obj_list, default_handler=str)
)
