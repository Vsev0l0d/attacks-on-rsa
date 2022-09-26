from utils import to_text

N = 78908333904637
e = 2821057
C = '''
66488995800290
61829195949215
75187156530365
66944513684556
15641889286263
25273508344802
33011686981708
63079735408371
71989137480846
15936556748887
35940951317181
65389528900590
'''

print(f'N = {N}\ne = {e}\nC = {C}\n')

n = ((N ** 0.5) // 1) + 1
print(f'n = [sqrt(N)] + 1 = {n}\n')
i = 0
while True:
    i += 1
    t = n + i
    print(f't{i} = n + {i} = {t}')
    w = (t ** 2) - N
    print(f'w{i} = t{i}**2 - N = {w}\n')
    if (w ** 0.5) % 1 == 0:
        print(f'sqrt(w{i}) = {w ** 0.5}\n')
        break

p = t + w ** 0.5
q = t - w ** 0.5
f = round((p - 1) * (q - 1))
d = pow(e, -1, f)

print(f'p = t{i} + sqrt(w{i}) = {p}')
print(f'q = t{i} - sqrt(w{i}) = {q}')
print(f'f = (p - 1) * (q - 1) = {f}')
print(f'd ≡ e^(-1) (mod f) = {d}\n')

message = ""
for i, c in enumerate(C.split()):
    m = pow(int(c), d, N)
    print(f'm{i} = {m}')
    message += to_text(m)

print(f'\nmessage = {message}')
