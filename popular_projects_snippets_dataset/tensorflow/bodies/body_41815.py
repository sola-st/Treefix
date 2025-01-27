# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
for v, init in initializers:
    v.assign(
        lift_to_graph.lift_to_graph([init], ops.get_default_graph())[init],
        read_value=False)
