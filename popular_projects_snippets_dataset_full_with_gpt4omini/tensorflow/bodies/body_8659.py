# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations.py
distributions = [
    v for v in kwargs.values() if isinstance(v, NamedDistribution)
]
required_gpus = kwargs.get("required_gpus", 0)
required_physical_gpus = kwargs.get("required_physical_gpus", 0)

if distributions and required_gpus:
    raise ValueError("Do not use `required_gpus` and arguments of type "
                     "NamedDistribution together.")

number_of_required_gpus = max(
    [required_gpus] + [required_physical_gpus] +
    [d.required_physical_gpus or 0 for d in distributions] +
    [d.required_gpus or 0 for d in distributions])
number_of_required_physical_gpus = max(
    [required_physical_gpus] +
    [d.required_physical_gpus or 0 for d in distributions])

if (required_physical_gpus and required_gpus):
    raise ValueError("Only one of `required_physical_gpus`(number of physical"
                     " GPUs required) and `required_gpus`(total number of "
                     "GPUs required) should be set. ")
if not number_of_required_gpus and GPUCombination.GPU_TEST:
    exit((False, "Test that doesn't require GPUs."))
elif (number_of_required_gpus > 0
      and context.num_gpus() < number_of_required_gpus):
    exit((False, ("Only {} of {} required GPUs are available.".format(
        context.num_gpus(), number_of_required_gpus))))
elif number_of_required_physical_gpus > len(
    config.list_physical_devices("GPU")):
    exit((False,
            ("Only {} of {} required physical GPUs are available.".format(
                config.list_physical_devices("GPU"), required_physical_gpus))))
else:
    exit((True, None))
