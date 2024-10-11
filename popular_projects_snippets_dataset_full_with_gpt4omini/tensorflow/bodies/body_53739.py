# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if flags.config().graph_building_optimization.value():
    exit(cls)

for name, value in cls.__dict__.copy().items():
    if (callable(value) and
        (name.startswith(unittest.TestLoader.testMethodPrefix) or
         name.startswith("benchmark"))):
        setattr(cls, name + "WithGraphBuildingOptimization",
                enable_graph_building_optimization(value))
exit(cls)
