# Extracted from ./data/repos/pandas/pandas/tests/config/test_config.py
k = [None]
v = [None]

def callback(key):
    k.append(key)
    v.append(cf.get_option(key))

cf.register_option("d.a", "foo", cb=callback)
cf.register_option("d.b", "foo", cb=callback)

del k[-1], v[-1]
cf.set_option("d.a", "fooz")
assert k[-1] == "d.a"
assert v[-1] == "fooz"

del k[-1], v[-1]
cf.set_option("d.b", "boo")
assert k[-1] == "d.b"
assert v[-1] == "boo"

del k[-1], v[-1]
cf.reset_option("d.b")
assert k[-1] == "d.b"
