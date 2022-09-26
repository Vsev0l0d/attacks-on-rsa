from decimal import *
from utils import to_text

N1 = 441716293693
N2 = 442258294987
N3 = 444399387571

C1 = '''
324500796659
324547036186
367901833181
38558700097
401956144715
260421328704
356041474179
113539876955
304515179769
302662240842
282367185538
432213853716
'''

C2 = '''
364411844182
137247785047
389030356498
293766643714
259139396276
429702138150
17968702271
84037113464
91988591941
425057692992
391906969363
244207991747
'''

C3 = '''
57065247639
130359065508
391859459727
128196485994
412050631244
367300386309
83703862830
218100297714
10243576841
232358719915
412546535924
398872645339
'''

print(f'N1 = {N1}\nN2 = {N2}\nN3 = {N3}\nC1 = {C1}\nC2 = {C2}\nC3 = {C3}\n')

M0 = N1 * N2 * N3
m1 = N2 * N3
m2 = N1 * N3
m3 = N2 * N1
n1 = pow(m1, -1, N1)
n2 = pow(m2, -1, N2)
n3 = pow(m3, -1, N3)

print(f'M0 = N1 * N2 * N3 = {M0}')
print(f'm1 = N2 * N3 = {m1}\nm2 = N1 * N3 = {m2}\nm3 = N2 * N1 = {m3}\n')
print(f'n1 ≡ m1^(-1) (mod N1) = {n1}\nn2 ≡ m2^(-1) (mod N2) = {n2}\nn3 ≡ m3^(-1) (mod N3) = {n3}\n')

c1 = list(map(int, C1.split()))
c2 = list(map(int, C2.split()))
c3 = list(map(int, C3.split()))

full_message = ''
for i in range(len(c1)):
    S = (c1[i] * n1 * m1) + (c2[i] * n2 * m2) + (c3[i] * n3 * m3)
    summodM0 = S % M0
    message = round(summodM0 ** (Decimal(1 / 3)))
    print(f'S{i} = c1[{i}]*n1*m1 + c2[{i}]*n2*m2 + c3[{i}]*n3*m3 = {S}')
    print(f'summodM0[{i}] = S{i} % M0 = {summodM0}\nmessage{i} = summodM0[{i}]^(1/3) = {message}\n')
    full_message += to_text(message)

print(f'\nfull_message = {full_message}')
