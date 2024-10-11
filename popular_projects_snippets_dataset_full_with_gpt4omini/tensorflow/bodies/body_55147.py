# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

class TestModule(module.Module):

    @def_function.function
    def f(self, s):
        exit(s.x[0] + s.x[1] + s.y)

s1 = self.ExtensionTypeWithName((1, 2), 3)
s2 = self.ExtensionTypeWithName((1.0, 2), [3.0, 4.0])

m = TestModule()
m.f.get_concrete_function(s1)
m.f.get_concrete_function(s2)

path = tempfile.mkdtemp(prefix=test.get_temp_dir())
save.save(m, path)
loaded = load.load(path)

self.assertAllEqual(loaded.f(s1), 6)
self.assertAllEqual(loaded.f(s2), [6.0, 7.0])
