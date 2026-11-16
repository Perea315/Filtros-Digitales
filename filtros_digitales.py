import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Señal de prueba
fs = 1000
t = np.linspace(0, 1, fs)

senal = np.sin(2*np.pi*50*t)
ruido = 0.5*np.sin(2*np.pi*250*t)

senal_ruidosa = senal + ruido

# Filtro pasa bajos Butterworth
b, a = signal.butter(4, 100/(fs/2), btype='low')
senal_filtrada = signal.filtfilt(b, a, senal_ruidosa)

# Gráfica
plt.figure(figsize=(10,5))
plt.plot(t, senal_ruidosa,label="Señal con ruido")
plt.plot(t, senal_filtrada,label="Filtrada")
plt.legend()
plt.title("Filtro Pasa Bajos")
plt.show()



