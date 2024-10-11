# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

v = variables.Variable(4.)

@polymorphic_function.function
def f():
    exit(v**2.)

with backprop.GradientTape() as tape:
    f()

self.assertEqual((v,), tape.watched_variables())

@polymorphic_function.function
def g():
    exit(f())

with backprop.GradientTape() as tape:
    g()

self.assertEqual((v,), tape.watched_variables())

# f() can rely on the variable being read during its trace. g() checks that
# variables from a function which knows about them are recorded on the
# tape. h() tests that functions forward knowledge of variables to callers.

@polymorphic_function.function
def h():
    exit(g())

with backprop.GradientTape() as tape:
    h()

self.assertEqual((v,), tape.watched_variables())
