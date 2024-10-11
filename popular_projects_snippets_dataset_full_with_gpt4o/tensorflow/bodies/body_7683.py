# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy(enable_packed_var)

with strategy.scope():
    tpu_vars = [variables.Variable(1)]

def only_star_args(*args):
    del args

def pos_and_star_args(first_arg, *args):
    del first_arg
    del args

def named_args(first_arg, second_arg):
    del first_arg
    del second_arg

def star_args_and_kw_only(*args, kw):
    del args
    del kw

# pylint:disable=function-redefined
@def_function.function
def step():
    strategy.run(only_star_args, args=(2,))

step()

@def_function.function
def step():
    strategy.run(named_args, kwargs={"first_arg": 2, "second_arg": 3})

step()

with self.assertRaisesRegex(TypeError, r"got multiple values for argument"):

    @def_function.function
    def step():
        strategy.run(
            named_args, args=(1,), kwargs={
                "first_arg": 2,
                "second_arg": 3
            })

    step()

with self.assertRaisesRegex(ValueError,
                            r"cannot handle Variables passed to \*args"):

    @def_function.function
    def step():
        strategy.run(
            only_star_args, args=(
                2,
                tpu_vars,
            ))

    step()

@def_function.function
def step():
    strategy.run(pos_and_star_args, args=(2, 3, 4))

step()

@def_function.function
def step():
    strategy.run(star_args_and_kw_only, args=(2, 3), kwargs={"kw": tpu_vars})

step()

with self.assertRaisesRegex(ValueError,
                            r"mix of positional args and \*args"):

    @def_function.function
    def step():
        strategy.run(pos_and_star_args, args=(tpu_vars, 3, 4))

    step()

with self.assertRaisesRegex(ValueError, r"Too many positional arguments"):

    @def_function.function
    def step():
        strategy.run(named_args, args=(2, 3, 4))

    step()

class DummyClass:

    @def_function.function
    def method(self, arg_1):
        del arg_1

    def step(self):
        strategy.run(self.method, args=(tpu_vars,))

DummyClass().step()
