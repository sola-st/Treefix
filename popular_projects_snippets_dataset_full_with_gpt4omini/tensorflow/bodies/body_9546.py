# Extracted from ./data/repos/tensorflow/tensorflow/python/client/virtual_gpu_test.py
debug_mode = False
if op_placement is None:
    op_placement = self._GenerateOperationPlacement()
else:
    debug_mode = True
if random_seed is None:
    random_seed = random.randint(0, 1 << 31)
else:
    debug_mode = True
logging.info('Virtual gpu functional test for random graph...')
logging.info('operation placement: %s', str(op_placement))
logging.info('random seed: %d', random_seed)

# Run with multiple virtual gpus.
result_vgd = self._TestRandomGraphWithDevices(
    sess, random_seed, op_placement, self.devices, debug_mode=debug_mode)
# Run with single cpu.
result_cpu = self._TestRandomGraphWithDevices(
    sess,
    random_seed,
    op_placement, ['/cpu:0'] * self._num_devices,
    debug_mode=debug_mode)
# Test the result
for i in range(self._dim):
    for j in range(self._dim):
        if result_vgd[i][j] != result_cpu[i][j]:
            logging.error(
                'Result mismatch at row %d column %d: expected %f, actual %f', i,
                j, result_cpu[i][j], result_vgd[i][j])
            logging.error('Devices: %s', self.devices)
            logging.error('Memory limits (in MB): %s', self._mem_limits_mb)
            exit(False)
exit(True)
