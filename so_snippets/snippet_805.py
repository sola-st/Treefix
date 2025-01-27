# Extracted from https://stackoverflow.com/questions/653509/breaking-out-of-nested-loops
for x in xrange(10):
    for y in xrange(10):
        print x*y
        if x*y > 50:
            break
    else:
        continue  # only executed if the inner loop did NOT break
    break  # only executed if the inner loop DID break

for x in xrange(10):
    for y in xrange(10):
        for z in xrange(10):
            print x,y,z
            if x*y*z == 30:
                break
        else:
            continue
        break
    else:
        continue
    break

