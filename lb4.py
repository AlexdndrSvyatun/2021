# 1
a = np.matrix([[2, 3, 1], [-1, 1, 0], [1, 2, -1]])
b = np.matrix([[1, 2, 1], [0, 1, 2], [3, 1, 1]])
sol = (a*b)-(b*a)
print('Answer :\n', sol)
# 2
c = np.matrix([[-1, 0, 2], [0, 1, 0], [1, 2, -1]])

print('Matrix : \n\n', np.linalg.matrix_power(c, 2))
# 3
d = np.matrix([[3,5],[6,-1]])
i = np.matrix([[6,1],[-3,2]])
print ('Answer :\n',d*i)
# 4
f = np.linalg.det([[2,3,4],[1,0,6],[7,8,9]])
print('Answer :\n',f)
# 5
f = np.matrix([[1, 5, -5], [4, 0, 3], [2, -10, 3]])
print ('Task 4. Var 5. \n')
print ('determinant: ', np.linalg.det(f))
print ('determinant rounded: ', round(np.linalg.det(f)) )
print ('_' * 70)
# 6
j = np.linalg-inv([[1,2,-3],[0.1,2],[0,0,1]])
print('Answer :\n',j)
# 7
k = np.linalg.matrix_rank([[1,2,3,4],[3,-1,2,5],[1.2,3,4],[1,3,4,5]])
print('Answer :\n',k)
# 8
q = np.matrix([[7, 3, -6], [7, 9, -9], [2, -4, 9]])
r = np.matrix([[-1, 5, 28]])

dets = []

det_q = np.linalg.det(q)

qi = copy.copy(q)

for i in range(len(qi)):

    for j in range(len(qi)):

        qi[j, i] = r[0, j]

    det_qi =  np.linalg.det(qi)
    dets.append(det_qi)
        
    qi = copy.copy(q)

print('Determinants:\n')
print(dets)

print("\nCramer:\n")

for i in range(len(q)):
    xi = dets[i]/det_q
    print(f'x{i+1} = {xi}')
# 9
j = np.matrix([[4, 1, 4], [1, 1, 2], [2, 1, 2]])
k = np.array([[-2], [-1], [0]])

det_j = round(np.linalg.det(j))


if (det_j == 0):
    print ("\nThere's no solution")

else:
    print ("\nmatrix: ")
    x1 = np.linalg.inv(j) * k
    print(x1)

    print ("\nsolution: ")
    x2 = np.linalg.solve(j,k)
    print(x2)
# 10
def task10():

    print('raws: ')
    n = int(input())

    print('colons: ')
    m = int(input())

    a = np.zeros((n, m))

    lim = n*m

    a0 = []

    i = 0

    while i < lim:

        a0.append(random.randint(0, 100))
        i+=1

    k = 0

    for i in range(n):
        for j in range(m):
            a[i, j] = a0[k]
            k+=1
            
    print('\nMatrix: \n')
    print(a)

    sum = 0

    for raw in a:
        for elem in raw:
            sum = sum + elem

    print('\n elements:')
    print(sum)

    for i in range(m):
        sumcol = 0
        for j in range(n):
            sumcol = sumcol + a[j, i]
            part = sumcol/sum
        print(f'\ncolonum sum {i+1}:')
        print(sumcol)
        print('general sum:')
        print(part)

task10()
