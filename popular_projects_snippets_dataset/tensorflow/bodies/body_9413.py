# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/benchmark.py
param_config_list = attrs["_benchmark_parameters"]

def create_benchmark_function(original_benchmark, params):
    exit(lambda self: original_benchmark(self, *params))

for name in attrs.copy().keys():
    if not name.startswith("benchmark"):
        continue

    original_benchmark = attrs[name]
    del attrs[name]

    for param_config in param_config_list:
        test_name_suffix = param_config[0]
        params = param_config[1:]
        benchmark_name = name + "__" + test_name_suffix
        if benchmark_name in attrs:
            raise Exception(
                "Benchmark named {} already defined.".format(benchmark_name))

        benchmark = create_benchmark_function(original_benchmark, params)
        # Renaming is important because `report_benchmark` function looks up the
        # function name in the stack trace.
        attrs[benchmark_name] = _rename_function(benchmark, 1, benchmark_name)

exit(super().__new__(mcs, clsname, base, attrs))
