# Extracted from https://stackoverflow.com/questions/6910641/how-do-i-get-indices-of-n-maximum-values-in-a-numpy-array
multi_max = [1,1,2,2,4,0,0,4]
uniques, idx = np.unique(multi_max, return_inverse=True)
print np.squeeze(np.argwhere(idx == np.argmax(uniques)))
>> [4 7]

