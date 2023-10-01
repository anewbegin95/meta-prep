# %%
import numpy as np

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Write your code here
    if not (1 <= N <= 200) or not (1 <= X <= Y <= N):
        raise ValueError("Resubmit valid values")
    
    valid_photo_count = 0
    photo_combo = []
    photo_range = range(N)
    distance_range = range(X, Y + 1)
    for x in photo_range:
        print(C[x])
        if C[x] == 'P':
            print(f"Found {C[x]}! It's the {x} character in the string")

            for dist in distance_range:
                check_after_p = C.index(C[x]) + dist
                if check_after_p < 0:
                    # print(f'Index is before the beginning of the string and out of range')
                    continue
                elif check_after_p >= N:
                    continue
                else:
                    pos_a_check = C[check_after_p]
                    # print(f'P is {dist} away from {pos_a_check}, the {check_after_p} character')
                
                    if pos_a_check == 'A':
                        # print(f'Found A {dist} away from P!')
                        
                        for dist2 in distance_range:
                            check_after_a = C.index(C[x]) + dist + dist2
                            if check_after_a < 0:
                                # print(f'Index is before the beginning of the string and out of range')
                                continue
                            elif check_after_a >= N:
                                continue
                            else:
                                pos_b_check = C[check_after_a]
                                # print(f'A is {dist2} away from {pos_b_check}, the {check_after_a} character')
                                if pos_b_check == 'B':
                                    # print(f'Found B {dist2} away from A! All conditions passed!')
                                    valid_photo_count += 1
                                    continue

                check_before_p = C.index(C[x]) - dist
                if check_before_p < 0:
                    print(f'Index is before the beginning of the string and out of range')
                    continue
                elif check_before_p >= N:
                    continue
                else:
                    neg_a_check = C[check_before_p]
                    print(f'P is {dist * -1} away from {neg_a_check}, the {check_before_p} character')

                    if neg_a_check == 'A':
                        print(f'Found A {dist * -1} away from P!')
                            
                        for dist2 in distance_range:
                            check_before_a = C.index(C[x]) - dist - dist2
                            if check_before_a < 0:
                                print(f'Index is before the beginning of the string and out of range')
                                continue
                            elif check_before_a >= N:
                                continue
                            else:
                                neg_b_check = C[check_before_a] 
                                print(f'A is {dist2 * -1} away from {neg_b_check}, the {check_before_a} character')

                                if neg_b_check == 'B':
                                    print(f'Found B {dist2 * -1} away from A! All conditions passed!')
                                    valid_photo_count += 1
                                    continue

    return valid_photo_count

# %%
N1, C1, X1, Y1 = 5, 'APABA', 1, 2
result1 = getArtisticPhotographCount(N1, C1, X1, Y1)
print(result1)
# %%
N2, C2, X2, Y2 = 5, 'APABA', 2, 3
result2 = getArtisticPhotographCount(N2, C2, X2, Y2)
print(result2)
# %%
N3, C3, X3, Y3 = 8, '.PBAAP.B', 1, 3
result3 = getArtisticPhotographCount(N3, C3, X3, Y3)
print(result3)
# %%
list = ['A', 'B', 'C']
x = 'B'
dist = 2
print(list[list.index(x) - dist])
# %%
