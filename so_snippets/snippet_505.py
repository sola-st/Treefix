# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/14770735/how-do-i-change-the-figure-size-with-subplots
from l3.Runtime import _l_
plt.figure(figsize=(16, 8)) 
_l_(2849) 
for i in range(1, 7):
    _l_(2853)

    plt.subplot(2, 3, i)
    _l_(2850)
    plt.title('Histogram of {}'.format(str(i)))
    _l_(2851)
    plt.hist(x[:,i-1], bins=60)
    _l_(2852)

