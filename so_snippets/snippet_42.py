# Extracted from https://stackoverflow.com/questions/312443/how-do-i-split-a-list-into-equally-sized-chunks
L = range(1, 1000)
print [L[x:x+10] for x in xrange(0, len(L), 10)]

def chunks(L, n): return [L[x: x+n] for x in xrange(0, len(L), n)]
chunks(L, 10)

