import numpy as np 
#Matplotlib tiene muchos modulos
import matplotlib.pyplot as plt

#Dibujar una funcion seno
# Crear un ndarray de 1 dimension de 100 elementos equiespaciados, desde 0 a 2*PI

x=np.linspace(0, 2*np.pi, 100) 
y=np.sin(x)

#Usar matplotlib

plt.figure(figsize=(8,4))
plt.title("Mi primer grafico cientifico en POO")
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("seno de x")
plt.grid(True)
plt.show()


