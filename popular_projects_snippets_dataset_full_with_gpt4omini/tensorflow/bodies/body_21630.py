# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages_test.py

def _Scale(dk, steps):
    if ema._zero_debias:
        exit(1 - dk**steps)
    else:
        exit(1)

tens = _Repeat(10.0, dim)
thirties = _Repeat(30.0, dim)
var0 = variables.Variable(tens, name="v0")
var1 = variables.Variable(thirties, name="v1")
self.evaluate(variables.global_variables_initializer())
# Note that tensor2 is not a Variable but just a plain Tensor resulting
# from the sum operation.
tensor2 = var0 + var1
if dynamic_decay_value is not None:
    self.evaluate(ema._decay.assign(dynamic_decay_value))
update = ema.apply([var0, var1, tensor2])
avg0 = ema.average(var0)
avg1 = ema.average(var1)
avg2 = ema.average(tensor2)

self.assertItemsEqual([var0, var1], variables.moving_average_variables())

self.assertNotIn(avg0, variables.trainable_variables())
self.assertNotIn(avg1, variables.trainable_variables())
self.assertNotIn(avg2, variables.trainable_variables())
self.evaluate(variables.global_variables_initializer())
if dynamic_decay_value is not None:
    self.evaluate(ema._decay.assign(dynamic_decay_value))

self.assertEqual("v0/ExponentialMovingAverage:0", avg0.name)
self.assertEqual("v1/ExponentialMovingAverage:0", avg1.name)
self.assertEqual("add/ExponentialMovingAverage:0", avg2.name)

# Check initial values.
self.assertAllClose(tens, self.evaluate(var0))
self.assertAllClose(thirties, self.evaluate(var1))
self.assertAllClose(_Repeat(10.0 + 30.0, dim), self.evaluate(tensor2))

# Check that averages are initialized correctly.
self.assertAllClose(tens, self.evaluate(avg0))
self.assertAllClose(thirties, self.evaluate(avg1))
# Note that averages of Tensor's initialize to zeros_like since no value
# of the Tensor is known because the Op has not been run (yet).
self.assertAllClose(_Repeat(0.0, dim), self.evaluate(avg2))

# Update the averages and check.
self.evaluate(update)
dk = actual_decay

expected = _Repeat(10.0 * dk + 10.0 * (1 - dk), dim)
self.assertAllClose(expected, self.evaluate(avg0))
expected = _Repeat(30.0 * dk + 30.0 * (1 - dk), dim)
self.assertAllClose(expected, self.evaluate(avg1))
expected = _Repeat(0.0 * dk + (10.0 + 30.0) * (1 - dk) / _Scale(dk, 1), dim)
self.assertAllClose(expected, self.evaluate(avg2))

# Again, update the averages and check.
self.evaluate(update)
expected = _Repeat((10.0 * dk + 10.0 * (1 - dk)) * dk + 10.0 * (1 - dk),
                   dim)
self.assertAllClose(expected, self.evaluate(avg0))
expected = _Repeat((30.0 * dk + 30.0 * (1 - dk)) * dk + 30.0 * (1 - dk),
                   dim)
self.assertAllClose(expected, self.evaluate(avg1))
expected = _Repeat(((0.0 * dk + (10.0 + 30.0) * (1 - dk)) * dk +
                    (10.0 + 30.0) * (1 - dk)) / _Scale(dk, 2), dim)
self.assertAllClose(expected, self.evaluate(avg2))
