# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 13:28:20 2024

@author: Florian Bethe
"""

from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector

def superdense_coding(bits):
    # Berechnen der Anzahl der benötigten Qubits
    num_qubits = (len(bits) // 2) + (len(bits) % 2)  # Zusätzliches Qubit für das überzählige Bit
    
    # Quantenkreis initialisieren
    qc = QuantumCircuit(2 * num_qubits)
    
    # Verschränkung für jedes Paar von Qubits erstellen
    for i in range(len(bits) // 2):  # Nur für die geraden Bits
        qc.h(i*2)  # Hadamard-Gate auf dem ersten Qubit des Paares anwenden
        qc.cx(i*2, i*2+1)  # CNOT-Gate zwischen den Qubits des Paares anwenden
    
    # Die Bits codieren
    for i in range(0, len(bits) - (len(bits) % 2), 2):  # Nur für die geraden Bits
        bit_pair = bits[i:i+2]
        
        # Entscheiden, welche Operationen angewendet werden sollen, basierend auf den Bits
        if bit_pair == [0, 0]:
            pass  # Keine zusätzliche Operation erforderlich
        elif bit_pair == [0, 1]:
            qc.x(i+1)
        elif bit_pair == [1, 0]:
            qc.z(i+1)
        elif bit_pair == [1, 1]:
            qc.x(i+1)
            qc.z(i+1)
    
    # Direkte Kodierung des letzten Bits, falls vorhanden
    if len(bits) % 2!= 0:
        last_bit_index = len(bits) - 1
        if bits[last_bit_index] == 1:
            qc.x(2 * num_qubits - 1)
    


    for i in range(len(bits) // 2):  # Nur für die geraden Bits
        qc.h(i*2+1)  # Hadamard-Gate auf dem ersten Qubit des Paares anwenden

    # if 0 != len(bits) % 2:
    #     qc.h(len(bits)//2+2)  # Hadamard-Gate auf dem ersten Qubit des Paares anwenden



    # Messungen vornehmen
    qc.measure_all()
    
    return qc

# Beispielaufruf der Funktion mit einer ungeraden Anzahl von Bits
bits_to_encode = [1, 0, 1, 1]  # Eine Sequenz mit ungerader Bitanzahl
qc = superdense_coding(bits_to_encode)
# qc.draw(output='mpl')  # Zeichnet das Quantenkreisschema

# Ausführung des Quantenkreises auf einem Simulator
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator)
result = job.result()

# Ergebnisse anzeigen
counts = result.get_counts(qc)
print("\nErgebnisse:", counts)
