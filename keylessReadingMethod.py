from utils import to_text

N = 319418480417
e1 = 602087
e2 = 523639

C1 = '''
52405618926
216147098445
216743861265
66972942908
191820297330
190353918873
110095200781
90183965366
296876615222
154988611456
166443759664
9906682687
'''

C2 = '''
82810335170
187684665216
48173641649
96024498047
247351492178
97241452868
255901558905
27364319220
227156630511
66990230889
183816391944
104719299259
'''


def gcd_extended(num1, num2):
    if num1 == 0:
        return num2, 0, 1
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return div, y - (num2 // num1) * x, x


print(f'N = {N}\ne1 = {e1}\ne2 = {e2}\nC1 = {C1}\nC2 = {C2}\n')

a, r, s = gcd_extended(e1, e2)
print(f'e1∙r + e2∙s = ±1\n\tr = {r}\n\ts = {s}\n')

c1 = tuple(map(int, C1.split()))
c2 = tuple(map(int, C2.split()))
message = ""
for i in range(len(c1)):
    c1r = pow(c1[i], r, N)
    c2s = pow(c2[i], s, N)
    m = c1r * c2s % N
    print(f'c1[{i}]^r (mod N) = {c1r}\nc2[{i}]^s (mod N) = {c2s}\nm{i} = {m}\n')
    message += to_text(m)

print(f'\nmessage = {message}')
