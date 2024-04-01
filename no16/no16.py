def recursive1(n):
    if n==1 : return 0
    return n * recursive1(n-1) #return n * recursive1(n) 에서 수정

def recursive2(n):
    if n==1 : return 1     # 종료조건을 추가한다.
    print('현재 n = ', n)
    return n * recursive2(n-1)

print(recursive2(4))