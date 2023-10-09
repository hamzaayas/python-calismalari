_list = [1,2,3]
_tuple = (1,'iki',True)
_tuple2 = (3,'dört',True)

print(type(_list))
print(type(_tuple))

print(len(_tuple))
print(len(_list))

_list[0]=5 
 # _tuple[0]=3 # "tuple" listedeki elemanlar degişmez.

# _list.append(3)
# print(_list)

print(_tuple.count(1))

print(_tuple + _tuple2)

_t = tuple([1,2,3])

print(type(_t))
print(_t)






