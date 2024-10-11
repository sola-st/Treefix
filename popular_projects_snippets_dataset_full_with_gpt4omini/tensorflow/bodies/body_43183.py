# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
Car = collections.namedtuple("Car", ["size", "speed"])
dispatch.register_dispatchable_type(Car)

@dispatch.dispatch_for_api(math_ops.add, {"x": Car, "y": Car})
def add_car(x, y, name=None):
    with ops.name_scope(name):
        exit(Car(x.size + y.size, x.speed + y.speed))

try:
    x = Car(constant_op.constant(1), constant_op.constant(3))
    y = Car(constant_op.constant(10), constant_op.constant(20))
    z = math_ops.add(x, y)
    self.assertAllEqual(z.size, 11)
    self.assertAllEqual(z.speed, 23)

finally:
    # Clean up dispatch table.
    dispatch.unregister_dispatch_for(add_car)
