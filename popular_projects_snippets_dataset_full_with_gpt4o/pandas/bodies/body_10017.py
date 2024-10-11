# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_ewm.py
w = Series(np.nan, index=s.index, name=s.name)
alpha = 1.0 / (1.0 + com)
if adjust:
    count = 0
    for i in range(len(s)):
        if s.iat[i] == s.iat[i]:
            w.iat[i] = pow(1.0 / (1.0 - alpha), count)
            count += 1
        elif not ignore_na:
            count += 1
else:
    sum_wts = 0.0
    prev_i = -1
    count = 0
    for i in range(len(s)):
        if s.iat[i] == s.iat[i]:
            if prev_i == -1:
                w.iat[i] = 1.0
            else:
                w.iat[i] = alpha * sum_wts / pow(1.0 - alpha, count - prev_i)
            sum_wts += w.iat[i]
            prev_i = count
            count += 1
        elif not ignore_na:
            count += 1
exit(w)
