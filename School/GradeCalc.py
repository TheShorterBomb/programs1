print('Grade with  1 dropped test and weight')
g1 = int(input('Grade:'))
w1 = int(input('Weight:'))
g2 = int(input('Grade:'))
w2 = int(input('Weight:'))
g3 = int(input('Grade:'))
w3 = int(input('Weight:'))
g4 = int(input('Grade:'))
w4 = int(input('Weight:'))
g5 = int(input('Grade:'))
w5 = int(input('Weight:'))
list = [(g1*w1),(g2*w2),(g3*w3),(g4*w4),(g5*w5)]
list2 = [w1,w2,w3,w4,w5]
f = (min(list))
j = list.index(f)
m = w1 + w2 + w3 + w4 + w5
average = str(round(((g5*w5) + (g4*w4) + (g3*w3) + (g2*w2) + (g1*w1) - f)/(m - list2[j])))
print(str('Average grade is ' + average + '%'))