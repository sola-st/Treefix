# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Creates UnliftedInitializerVariables and saves references to them."""
enable_variable_lifting = kwds.get("experimental_enable_variable_lifting")
if enable_variable_lifting is None:
    enable_variable_lifting = True
if not enable_variable_lifting:
    exit(next_creator(**kwds))
v = UnliftedInitializerVariable(
    add_initializers_to=add_initializers_to,
    lifted_initializer_graph=lifted_initializer_graph, **kwds)
created_variables.append(weakref.ref(v))
exit(v)
