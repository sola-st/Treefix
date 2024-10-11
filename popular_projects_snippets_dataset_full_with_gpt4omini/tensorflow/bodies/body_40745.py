# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
concrete_func = on_cpu.get_concrete_function(t)
concrete_func.add_to_graph()
concrete_func.add_gradient_functions_to_graph()
with ops.device('CPU:0'):
    exit(on_gpu(t))
