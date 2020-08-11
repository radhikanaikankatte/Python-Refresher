from numpy import *
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])

m = reshape(a,(7,5))

print(m)

print(m[2])

print(m[3][3])

m_r = append(m,[['Avg',13,15,19,16]],0)

print(m_r)

m_i = insert(m,2,['test',5,7,8,0],0)

print(m_i)

m_d = delete(m_i,2,0)

print(m_d)

m[3] = ['Thu',0,0,0,0]

print(m)


