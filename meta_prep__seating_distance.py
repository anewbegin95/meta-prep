"""
A cafeteria table consists of a row of  N seats, numbered from 1 to N from left 
to right. Social distancing guidelines require that every diner be seated such that
K seats to their left and K seats to their right (or all the remaining seats to 
that side if there are fewer than K) remain empty.

There are currently M diners seated at the table, the ith of whom is in seat 
Si. No two diners are sitting in the same seat, and the social distancing guidelines
are satisfied. Determine the maximum number of additional diners who can potentially
sit at the table without social distancing guidelines being violated for any new or
existing diners, assuming that the existing diners cannot move and that the 
additional diners will cooperate to maximize how many of them can sit down.
Please take care to write a solution which runs within the time limit.

Constraints:
1 ≤ N ≤ 10 ** 15
1 ≤ K ≤ N
1 ≤ M ≤ 500,000
M ≤ N
1 ≤ Si ≤ N

Sample test case #1
N = 10
K = 1
M = 2
S = [2, 6]
Expected Return Value = 3

Sample test case #2
N = 15
K = 2
M = 3
S = [11, 6, 14]
Expected Return Value = 1

Sample Explanation
In the first case, the cafeteria table has N=10 seats, with two diners currently 
at seats 2 and 6 respectively. The table initially looks as follows, with brackets
covering the K = 1 seat to the left and right of each existing diner that may not 
be taken.
  [1 2 3] 4 [5 6 7] 8 9 10
Three additional diners may sit at seats 4, 8, and 10 without violating the social
distancing guidelines. In the second case, only 1 additional diner is able to join 
the table, by sitting in any of the first 3 seats.
"""
# %%
from typing import List

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    if not (1 <= N <= 10**15) or not (1 <= K <= N) or not (1 <= M <= 500000) or M > N:
        raise ValueError("Input values out of range")
    
    S = sorted(S)
    available_seats = []

    # Check if there's space before the first diner
    space_before_first = S[0] - K - 1
    if space_before_first >= 0:
        for i in range(1, S[0] - K):
            available_seats.append(i)

    # Check if there's space between diners
    for i in range(1, M):
        space_between = S[i] - S[i-1] - 2*K - 1
        if space_between >= 0:
            for j in range(S[i-1] + K + 1, S[i] - K):
                available_seats.append(j)

    # Check if there's space after the last diner
    space_after_last = N - S[-1] - K
    if space_after_last >= 0:
        for i in range(S[-1] + K + 1, N + 1):
            available_seats.append(i)

    optimized_seats = available_seats

    for x in optimized_seats:
        for Ki in range(1, K+1):
            if (x - Ki in available_seats) and (x + Ki in available_seats):
                optimized_seats.remove(x)
            elif (x - Ki in available_seats):
                optimized_seats.remove(x - Ki)
            elif (x + Ki in available_seats):
                optimized_seats.remove(x + Ki)

    return len(optimized_seats)

# Sample test cases
N1, K1, M1, S1 = 10, 1, 2, [2, 6]
N2, K2, M2, S2 = 15, 2, 3, [11, 6, 14]

result1 = getMaxAdditionalDinersCount(N1, K1, M1, S1)
result2 = getMaxAdditionalDinersCount(N2, K2, M2, S2)

print(result1)  # Output: 3
print(result2)  # Output: 1

# %%
