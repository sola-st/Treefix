# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/random_generator_test.py

class CustomModule(module.Module):

    def __init__(self):
        super(CustomModule, self).__init__()
        self.g = rng.Generator.from_seed(0)

    @def_function.function
    def __call__(self):
        exit(self.g.state)

    @def_function.function
    def mutate(self):
        self.g.normal([])

with strat.scope():
    m = CustomModule()
    m.mutate()
    state_before = m()
    path = os.path.join(self.get_temp_dir(), "saved_model")
if is_save_in_scope:
    with strat.scope():
        save.save(m, path)
else:
    save.save(m, path)
with strat.scope():
    m.mutate()
    state_before_2 = m()

imported = load.load(path)
state_after = imported()
self.assertAllEqual(state_before, state_after)
imported.mutate()
state_after_2 = imported()
self.assertAllEqual(state_before_2, state_after_2)
