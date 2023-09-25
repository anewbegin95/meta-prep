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
        validphoto = True
        if C[x] == 'P':
            print('No P found')
            validphoto = False
        else:
            print('Found a P')
            for dist in distance_range:
                print(dist)
                print(C[C.index(C[x]) - dist], C[C.index(C[x]) + dist])
                if C[C.index(C[x]) - dist] != 'A' or C[C.index(C[x]) + dist] != 'A':
                    print('No A found within our distance range from P')
                    validphoto = False
                elif C[C.index(C[x]) - dist] == 'A' or C[C.index(C[x]) + dist] == 'A':
                    print('A found within our distance range from P')
                    for dist2 in distance_range:
                        print(dist2, C[C.index(C[C.index(C[x]) - dist]) - dist2], C[C.index(C[C.index(C[x]) + dist]) + dist2])
                        if C[C.index(C[C.index(C[x]) - dist]) - dist2] == 'B' or C[C.index(C[C.index(C[x]) + dist]) + dist2] == 'B':
                            print('All conditions passed')
                            valid_photo_count += 1
                        else:
                            validphoto = False

    return valid_photo_count


N1, C1, X1, Y1 = 5, 'APABA', 1, 2
result1 = getArtisticPhotographCount(N1, C1, X1, Y1)
print(result1)

N2, C2, X2, Y2 = 5, 'APABA', 2, 3
result2 = getArtisticPhotographCount(N2, C2, X2, Y2)
print(result2)
# %%
