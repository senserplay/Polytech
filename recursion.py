def task1(n,cur=1):
    if cur>n:
        return
    print(cur)
    task1(n,cur+1)

def task2(A,B):
    if A==B:
        print(A)
        return
    print(A)
    if A<B:
        task2(A+1,B)
    else:
        task2(A-1,B)


def task_3(num, ans=2, res=[]):
    if num < ans * ans:
        print(res + [num])
        return
    if num % ans == 0:
        return task_3(num // ans, ans, res + [ans])
    else:
        return task_3(num, ans + 1, res)


#Задание 1
n=int(input("Введите n: "))
task1(n)

#Задание 2
print("Введите A,B: ")
A,B=int(input()),int(input())
task2(A,B)

#Задание 3
n=int(input("Введите n: "))
task_3(n)

