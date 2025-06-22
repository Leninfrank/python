tpl = (20,30,40,'xyz')

print(tpl)

#tuple cannot be changed

print(tpl*3)
print(tpl.count(20))
print(tpl.index('xyz'))

lst=[67,34,'xyz']
print(type(lst))
tpl1=tuple(lst)
print(tpl)