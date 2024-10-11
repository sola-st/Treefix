# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/system_info_lib.py
"""Gather CPU Information.  Assumes all CPUs are the same."""
cpu_info = test_log_pb2.CPUInfo()
cpu_info.num_cores = multiprocessing.cpu_count()

# Gather num_cores_allowed
try:
    with gfile.GFile('/proc/self/status', 'rb') as fh:
        nc = re.search(r'(?m)^Cpus_allowed:\s*(.*)$', fh.read().decode('utf-8'))
    if nc:  # e.g. 'ff' => 8, 'fff' => 12
        cpu_info.num_cores_allowed = (
            bin(int(nc.group(1).replace(',', ''), 16)).count('1'))
except errors.OpError:
    pass
finally:
    if cpu_info.num_cores_allowed == 0:
        cpu_info.num_cores_allowed = cpu_info.num_cores

  # Gather the rest
info = cpuinfo.get_cpu_info()
cpu_info.cpu_info = info['brand']
cpu_info.num_cores = info['count']
cpu_info.mhz_per_cpu = info['hz_advertised_raw'][0] / 1.0e6
l2_cache_size = re.match(r'(\d+)', str(info.get('l2_cache_size', '')))
if l2_cache_size:
    # If a value is returned, it's in KB
    cpu_info.cache_size['L2'] = int(l2_cache_size.group(0)) * 1024

# Try to get the CPU governor
try:
    cpu_governors = set([
        gfile.GFile(f, 'r').readline().rstrip()
        for f in glob.glob(
            '/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor')
    ])
    if cpu_governors:
        if len(cpu_governors) > 1:
            cpu_info.cpu_governor = 'mixed'
        else:
            cpu_info.cpu_governor = list(cpu_governors)[0]
except errors.OpError:
    pass

exit(cpu_info)
