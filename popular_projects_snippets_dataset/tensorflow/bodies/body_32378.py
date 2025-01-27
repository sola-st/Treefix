# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/reconstruction_ops_test.py
super(ReconstructionOpsTest, self).__init__(*args, **kwargs)
self.batch_size = 3
self.frames = 3
self.samples = 5

self.bases = np.array(range(2, 5))
exponents = np.array(range(self.frames * self.samples))
powers = np.power(self.bases[:, np.newaxis], exponents[np.newaxis, :])

self.powers = np.reshape(powers, [self.batch_size, self.frames,
                                  self.samples])
self.frame_hop = 2

# Hand computed example using powers of unique numbers: this is easily
# verified.
self.expected_string = ["1", "10", "100100", "1001000", "10010010000",
                        "100100000000", "1001000000000", "10000000000000",
                        "100000000000000"]
