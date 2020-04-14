import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
dataset = pd.read_csv(r"C:\Users\BARANI\Desktop\cereal.csv")
dataset.head()
A=dataset['X'].values.reshape(-1,1)
B=dataset['Y'].values.reshape(-1,1)
model = LinearRegression()
model.fit(A,B)

plt.figure()
plt.title('House Price in Sanfransisco')
plt.xlabel('House (Bedrooms)')
plt.ylabel('Price (Crores)')
plt.plot(A,B,'.')
plt.plot(A,model.predict(A),'--')
plt.axis([0,10,0,10])
plt.grid(True)
plt.show()

print ("Predicted price = ",model.predict([[6]]))
