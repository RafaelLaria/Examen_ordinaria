import numpy as np
import matplotlib.pyplot as plt

class AnalizadorSismico:
    def __init__(self, sensor : str):
        self.sensor = sensor
        self.datos = []
    
    def __str__(self):
        return f'Nombre del Sensor: {self.sensor}'
    
    def cargar_datos(self):
        with open('sismo_data.txt', 'r') as f:
            for num in f:
                num = num.strip()
                try:
                    dato = float(num)
                    self.datos.append(dato)
                except ValueError:
                    continue

        self.datos = np.array(self.datos)
        return self.datos
    
    def analizar_riesgo(self):
        media = np.mean(self.datos)
        print(media)
        maximo = np.max(self.datos)
        print(maximo)
        if maximo > 7.0:
            print('ALERTA ROJA')
        elif 4.0 < maximo < 7.0:
            print('ALERTA AMARILLA')
        else:
            print('NORMAL')
    
    def generar_grafico(self):
        plt.plot(self.datos)
        plt.show()


sensor1 = AnalizadorSismico('BuscaNegros')
sensor1.cargar_datos()
riesgo = sensor1.analizar_riesgo()
print(f'Nivel de riesgo: {riesgo}')

sensor1.generar_grafico()
