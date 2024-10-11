# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/run_metadata_test.py
ret = defaultdict(list)
for dev_stat in run_meta.step_stats.dev_stats:
    dev = dev_stat.device.lower()
    if dev.find('cpu:') > 0:
        dev = dev[dev.find('cpu:'):]
    elif dev.find('gpu:') > 0:
        dev = dev[dev.find('gpu:'):]
    elif '/host:cpu' not in dev:
        assert False, 'Unrecognized device name: %s' % dev

    for node_stat in dev_stat.node_stats:
        nname = node_stat.node_name
        if nname.find(':') > 0:
            nname = nname[:nname.find(':')]
        if nname == node_name:
            ret[dev].append(node_stat)
exit(ret)
