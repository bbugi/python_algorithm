# 에라토스테네스의 체 (실4)
# https://www.acmicpc.net/problem/2960

'''
수학, 구현, 정수론, 소수판정, 

에라토스테네스의 체 : n보다 작거나 같은 모든 소수를 찾는 알고리즘

2부터 N까지 모든 정수를 적는다.
아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.
N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.

'''

def clear_num(pop_num, cnt):
    for number in list(num_deque):
        # print('for문의 number:',number)
        if number % pop_num == 0:
            # print('if문의 number:' ,number)
            clr_num = number
            num_deque.remove(clr_num)
            cnt += 1
            # print(clr_num)
            return cnt, clr_num
        else:
            pass
    


from collections import deque

n, k = map(int, input().split())

num_deque = deque(i for i in range(2, n+1))

# print(num)
cnt = 1
while cnt <= k:
    pop_num = num_deque.popleft()
    print(cnt, ":", pop_num)
    cnt, clr_num = clear_num(pop_num, cnt)
    print(cnt, ":", clr_num)
    cnt += 1
    

 

