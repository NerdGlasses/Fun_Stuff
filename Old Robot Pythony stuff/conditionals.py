def add (input, input2):
    return (input + input2)
print (add(5,345))
print (add(4,12))

def sub (i,s):
    return (i-s)
print (add (5,sub(20,30)))

def m (h,g):
    return (h*g)
print (m(5, add (5,sub(20,30))))

def div (j,r):
    return (j/r)
print (div(5, m(5, add (5,sub(20,30)))))

def xp (e,t):
    return (e**t)
print (xp(5,div(5, m(5, add (5,sub(20,30))))))
print (add(5,xp(5,div(5, m(5, add (5,sub(20,30)))))))
print (sub(5,add(5,xp(5,div(5, m(5, add (5,sub(20,30))))))))
print (m(5, sub(5,add(5,xp(5,div(5, m(5, add (5,sub(20,30)))))))))
print (div(5,m(5, sub(5,add(5,xp(5,div(5, m(5, add (5,sub(20,30))))))))))
print (xp(5,div(5,m(5, sub(5,add(5,xp(5,div(5, m(5, add (5,sub(20,30)))))))))))
print (add(5,5)*sub(10,3))
