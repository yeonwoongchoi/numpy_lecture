import numpy as np

a =np.arange(15).reshape(3,5) #reshape = 행렬을 만들어 줌
b =np.array([2,3,4])
# print(a)
# print(type(a))
# print(a.shape)

# print(a.ndim)
print(b.dtype)


n_arr = np.array(range(1,11), dtype ='int32')
# n_arr.size
# print(n_arr.size)
data_size = n_arr.size * n_arr.itemsize
print(n_arr.itme size)
print(n_arr)
p_num = np.random.rand(range(1,10))
print(p_num)