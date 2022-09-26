from utils import to_text

C = '''
90401727778
50205386780
66796441575
1200754589
25390276538
64927766600
89595489304
12806265575
95100428023
7746226795
126261029912
66580024238
118827632497
'''

N = 144050016983
e = 1163719

for y in list(map(int, C.split())):
    yi = pow(y, e, N)
    while yi != y:
        res = yi
        yi = pow(yi, e, N)
    print(to_text(res), end='')
