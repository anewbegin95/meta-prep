#%%
import matplotlib.pyplot as plt
import pandas as pd

csv = 'study_info.csv'

df = pd.read_csv(csv)

study_time = df['study_time'].tolist()
exam_score = df['exam_score'].tolist()
# %%
plt.scatter(study_time, exam_score)
plt.title('Relationship between study time and exam score')
plt.xlabel('Total study time (in minutes)')
plt.ylabel('Exam score')
plt.show()
# %%
def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].study_time
        y = points.iloc[i].exam_score
        total_error += (y - ((m * x) + b)) ** 2
    return total_error / float(len(points))
# %%
def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].study_time
        y = points.iloc[i].exam_score

        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))
    
    m = m_now - m_gradient * L
    b = b_now - b_gradient * L

    return m, b
# %%
m = 0
b = 0
L = 0.001
epochs = 100

for i in range(epochs):
    m, b = gradient_descent(m, b, df, L)

print(m, b)
plt.scatter(df.study_time, df.exam_score, color="Black")
plt.plot(list(range(45, 350)), [m * x + b for x in range(45, 350)], color="Red")
plt.show()
# %%
