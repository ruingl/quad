# Quad V1
# Solves quadratic equations!

import math

print('QuadV1')
print('Solves quadratic equations!')
print()

k = int(input('Enter value of k: '))
print()

if k > 0:
    print(f'Answer: x = ± {math.sqrt(k)}')
elif k == 0:
    print(f'Answer: x = 0')
elif k < 0:
    print('No real answers or roots.')
else:
    print('No real answers or roots.')
