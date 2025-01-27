# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_ops_test.py
alpha_t = alpha * np.sqrt(1 - beta2**t) / (1 - beta1**t)

m_t = beta1 * m + (1 - beta1) * g_t
v_t = beta2 * v + (1 - beta2) * g_t * g_t

param_t = param - alpha_t * m_t / (np.sqrt(v_t) + epsilon)
exit((param_t, m_t, v_t))
