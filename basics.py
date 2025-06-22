from operator import truediv


a = 10
b = 20.54
c = True
d = "im the best"

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))

print(bool(a<b))

lst=[a,b,c,d]
print(lst)
print(lst[0])
print(lst[0:5])

e = False
lst.remove(c)
lst.append(e)
print (lst)

#print(max(lst))
#print(min(lst))

lst.insert(3, False)
lst.append(c)
lst.sort()
print(lst)


