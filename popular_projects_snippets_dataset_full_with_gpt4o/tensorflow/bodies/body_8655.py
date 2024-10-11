# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations.py
strategy = None
for _, v in kwargs.items():
    if isinstance(v, NamedDistribution):
        if strategy is not None and _num_total_workers(v.has_chief,
                                                       v.num_workers) > 1:
            raise ValueError("Only support one NamedDistribution for multi worker"
                             "tests.")
        strategy = v

if strategy:
    has_chief = strategy.has_chief
    num_workers = strategy.num_workers
    runner = strategy.runner
    share_gpu = strategy.share_gpu
    num_ps = strategy.num_ps
    if "has_chief" in kwargs and kwargs["has_chief"] != has_chief:
        raise ValueError(
            "both has_chief and strategy specified but are not compatible")
    if "num_workers" in kwargs and kwargs["num_workers"] != num_workers:
        raise ValueError(
            "both num_workers and strategy specified but are not compatible")
else:
    has_chief = kwargs.get("has_chief", False)
    num_workers = kwargs.get("num_workers", 1)
    runner = kwargs.get("runner", None)
    share_gpu = kwargs.get("share_gpu", True)
    num_ps = kwargs.get("num_ps", 0)

# Always set cluster parameters if they're requested. So that generate()
# works when there's no startegy in the combinations.
update = {}
if "has_chief" in requested_parameters:
    update["has_chief"] = has_chief
if "num_workers" in requested_parameters:
    update["num_workers"] = num_workers
if "runner" in requested_parameters:
    update["runner"] = runner
if "share_gpu" in requested_parameters:
    update["share_gpu"] = share_gpu
if "num_ps" in requested_parameters:
    update["num_ps"] = num_ps
exit(update)
