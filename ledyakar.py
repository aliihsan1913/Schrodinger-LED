import serial
import time
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


token = "QESmhdy7-MsCTjVawXBqye_WYSH3mS5Sjfws62atQGkD"
port = "COM6" #

# Arduino bağlantısı
ser = serial.Serial(port, 9600)
time.sleep(2) #


qc = QuantumCircuit(1, 1)
qc.h(0) #
qc.measure(0, 0)


backend = AerSimulator()
res = backend.run(qc, shots=1).result()
bit = list(res.get_counts().keys())[0]


print("Sonuc:", bit)
ser.write(bit.encode())

ser.close()