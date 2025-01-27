# Extracted from ./data/repos/pandas/pandas/_testing/contexts.py

self.start_state = np.random.get_state()
np.random.seed(self.seed)
