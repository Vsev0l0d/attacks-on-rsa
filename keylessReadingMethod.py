from utils import print_number_to_text

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


a, r, s = gcd_extended(e1, e2)
y1 = list(map(int, C1.split()))
y2 = list(map(int, C2.split()))
for i in range(len(y1)):
    print_number_to_text(pow(y1[i], r, N) * pow(y2[i], s, N) % N)
