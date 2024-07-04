# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 10:16:48 2024

@author: Florian Bethe
"""

## libraries
"""
    qiskit              0.46.0
    qiskit-aer          0.14.2
    qiskit-ibm-runtime  0.23.0
    qiskit-terra        0.46.0
"""

## create QuantumCircuit
# leeren Quantenschaltkreis mit 3 Qubits und 2 klassischen Bits erstellen
"""
    qc = QuantumCircuit(3, 2) # 1. Anzahl Quantenbits, 2. Anzahl klassische Bits
"""

# The Hadamard gate equalizes the odds for each value of this qubit
"""
    qc.h(0)
"""

## entangle qubits
# CNOT - controlled NOT
# entanglement by controlled not gatter
"""
    qc.cx(0, 1)
"""


## C-pahse-flip-gate
# controlled phase-flip-gate
"""
    qc.z(0)

    q1 = |0>
    q2 = |1>
    
    q = 0.3 |0> + 0.7 |1>
    C-phase-flip gate
    q = 0.3 |0> - 0.7 |1>
"""

