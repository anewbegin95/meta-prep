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
        if C[x] == 'P':
            print(f'Found {C[x]}!')

            for dist in distance_range:
                pos_a_check = C[C.index(C[x]) + dist] 
                neg_a_check = C[C.index(C[x]) - dist] 
                print(f'P is {dist} away from {pos_a_check} and {neg_a_check}')

                if pos_a_check == 'A' or neg_a_check == 'A':
                    print(f'Found A {dist} away from P!')
                    
                    for dist2 in distance_range:
                        pos_b_check = C[C.index(pos_a_check) + dist2] 
                        neg_b_check = C[C.index(neg_a_check) - dist2] 
                        print(f'A is {dist2} away from {pos_a_check} and {neg_a_check}')

                        if pos_b_check == 'B' or neg_b_check == 'B':
                            print(f'Found B {dist} away from A! All conditions passed!')
                            valid_photo_count += 1


                #         print(dist2, C[C.index(C[C.index(C[x]) - dist]) - dist2], C[C.index(C[C.index(C[x]) + dist]) + dist2])
                #         if C[C.index(C[C.index(C[x]) - dist]) - dist2] == 'B' or C[C.index(C[C.index(C[x]) + dist]) + dist2] == 'B':
                #             print('All conditions passed!')
                #             valid_photo_count += 1

                # elif pos_b_check != 'A' or neg_b_check != 'A':
                #     print('No A found within our distance range from P')
                #     break
                #     for dist2 in distance_range:
                #         print(dist2, C[C.index(C[C.index(C[x]) - dist]) - dist2], C[C.index(C[C.index(C[x]) + dist]) + dist2])
                #         if C[C.index(C[C.index(C[x]) - dist]) - dist2] == 'B' or C[C.index(C[C.index(C[x]) + dist]) + dist2] == 'B':
                #             print('All conditions passed!')
                #             valid_photo_count += 1
                #         else:
                #             validphoto = False

    return valid_photo_count


N1, C1, X1, Y1 = 5, 'APABA', 1, 2
result1 = getArtisticPhotographCount(N1, C1, X1, Y1)
print(result1)

# N2, C2, X2, Y2 = 5, 'APABA', 2, 3
# result2 = getArtisticPhotographCount(N2, C2, X2, Y2)
# print(result2)
# %%
list = ['A', 'B', 'C']
x = 'B'
dist = 2
print(list[list.index(x) - dist])
# %%
