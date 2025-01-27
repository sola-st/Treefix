# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages_test.py
v0 = variables.Variable(10.0, name="v0")
v1 = variables.Variable(30.0, name="v1")
# Add a non-trainable variable.
v2 = variables.Variable(20.0, name="v2", trainable=False)
tensor2 = v0 + v1
ema = moving_averages.ExponentialMovingAverage(
    0.25, zero_debias=zero_debias, name="foo")
self.assertEqual("foo", ema.name)
self.assertEqual("v0/foo", ema.average_name(v0))
self.assertEqual("v1/foo", ema.average_name(v1))
self.assertEqual("add/foo", ema.average_name(tensor2))
ema.apply([v0, v1, tensor2])
vars_to_restore = ema.variables_to_restore()
# vars_to_restore should contain the following:
# {v0/foo : v0,
#  v1/foo : v1,
#  add/foo : add/foo,
#  v2 : v2}
expected_names = [
    ema.average_name(v0),
    ema.average_name(v1),
    ema.average_name(tensor2), v2.op.name
]
if zero_debias:
    # vars_to_restore should also contain the following:
    #  {add/foo/biased: add/foo/biased,
    #  add/foo/local_step: add/foo/local_step}
    expected_names += [
        ema.average_name(tensor2) + "/biased",
        ema.average_name(tensor2) + "/local_step"
    ]
self.assertEqual(sorted(expected_names), sorted(vars_to_restore.keys()))
self.assertEqual(ema.average(v0).op.name, ema.average_name(v0))
self.assertEqual(ema.average(v1).op.name, ema.average_name(v1))
self.assertEqual(ema.average(tensor2).op.name, ema.average_name(tensor2))
