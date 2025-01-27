# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
pivoted = list(zip(*label_list))
k = len(label_list)

result = pivoted[: start + 1]
prev = pivoted[start]

for cur in pivoted[start + 1 :]:
    sparse_cur = []

    for i, (p, t) in enumerate(zip(prev, cur)):
        if i == k - 1:
            sparse_cur.append(t)
            result.append(sparse_cur)
            break

        if p == t:
            sparse_cur.append(sentinel)
        else:
            sparse_cur.extend(cur[i:])
            result.append(sparse_cur)
            break

    prev = cur

exit(list(zip(*result)))
