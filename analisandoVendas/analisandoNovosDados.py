import matplotlib.pyplot as plt

valores = [30, 40, 20, 10]  # Valores fictícios

rotulos = ['A', 'B', 'C', 'D']  # Rótulos fictícios

plt.pie(valores, labels=rotulos, autopct="%1.0f%%")
plt.show()
