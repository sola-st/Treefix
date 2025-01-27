# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
new_func = [f for f in new_funcs if f.name == func.name]
self.assertEqual(len(new_func), 1)
self.expectFunctionsEqual(func, new_func=new_func[0])
