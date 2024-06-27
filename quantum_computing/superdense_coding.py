# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 09:20:05 2024

    SUPERDENSE CODING

Aufgabe:

    Alice hat 2 klassische Bits
    Alice hat auch einen Quantenbit
    Alice packt Information der 2 klassischen Bits in ein Quantenbit
    Diesen Quantenbit schickt sie dann über Quantenkanal an Bob
    Bob kriegt den Quantenbit
    Bob misst sowohl den erhaltenen Quantenbit als auch seinen eigenen 
    (welcher verschränkt ist mit dem erhaltenen Quantenbit)
 
    - Encode the information of 2 classical bits in 1 qubit
    - Qubit is then transported via a quantum channel


    STEPS

        1. Entangle q0 and q1
           - Alice gets q0 and Bob gets q1 
           - apply Hadamard gate to q0
           - apply CNOT gate to q1 with q0 as a control qubit

        2. If 1st bit is 1 apply phase flip to q0 (qc.z())
           - If 1st bit is 0 q0 remains unchanged

        3. If 2nd bit is 1 apply NOT gate to q0 (qc.x())
           - If 2nd bit is 0 q0 remains unchanged

        4. Send q0 via Quantum Channel to Bob

        5. Bob applies CNOT to q1 with q0 as a control qubit

        6. Bob applies Hadamard to q0

        7. Bob measures q0 and q1



    TODO: Implement base request for transport of two bits
    TODO: enhance implentation for transport of n bits
    TODO: enhance implentation for transport of text messages
    TODO: write a messenger application using this mechanism for communication


@author: Florian Bethe
"""
# Clear console
#       https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
#       https://hellocoding.de/blog/coding-language/python/farben-im-terminal
import colorama
colorama.init(autoreset=True)
print("\033[H\033[J", end="")
colorama.deinit()

import random

#   WARNINGS
import warnings
# Suppress or reset warings
warnings.filterwarnings("ignore")
# warnings.resetwarnings()

#   QISKIT
from qiskit import QuantumCircuit, Aer, execute, visualization
# from qiskit.visualization import circuit_drawer, plot_histogram



def get_entangled_qubits(num_qubits:int=2, num_cbits:int=1):
    """
    Create a quantum circuit with num_qubits entengled qubits having num_cbits
    classical bits each.

    Parameters
    ----------
    num_qubits : int, optional
        DESCRIPTION. The default is 2.
    num_cbits : int, optional
        DESCRIPTION. The default is 1.

    Returns
    -------
    Quantum circuit with entangled qubits.

    """
    qc = QuantumCircuit(num_qubits, num_cbits)
    
    # Entangle the qubits with each other.
    # TODO: Currently, excatly two qubits are entangled. Implement the entanglement of n qubits.

    """
        1. Entangle q0 and q1
           - Alice gets q0 and Bob gets q1 
           - apply Hadamard gate to q0
           - apply CNOT gate to q1 with q0 as a control qubit
    """
    
    # The Hadamard gate equalizes the odds for each value of this qubit
    qc.h(0)
    # entanglement by controlled not gatter
    qc.cx(0, 1)
    
    return qc


def superdense_encode_bits2qubit(qc:QuantumCircuit=None, bits:list=[0,0]):
    """
    
    !!! CURRENTLY just implemented for exactly two bits!

    Parameters
    ----------
    bits : list, optional
        DESCRIPTION. The default is [0].

    Returns
    -------
    qc : TYPE
        DESCRIPTION.

    """

    if True:
        if 1 == bits[0]:
            # 2. If 1st bit is 1 apply phase flip to q0 (qc.z())
            #    - If 1st bit is 0 q0 remains unchanged
            qc.z(0)
            
        if 1 == bits[1]:
            # 3. If 2nd bit is 1 apply NOT gate to q0 (qc.x())
            #     - If 2nd bit is 0 q0 remains unchanged
            qc.x(0)

    else:
        if bits[0] == 0 and bits[1] == 0:
            qc.x(0)
        elif bits[0] == 0 and bits[1] == 1:
            qc.z(0)
        elif bits[0] == 1 and bits[1] == 0:
            qc.x(0)
            qc.z(0)
        else: # bits[0] == 1 and bits[1] == 1
            qc.x(0)
    
        # Messung der Qubits
        qc.measure_all()
    
    return qc


def superdense_decode_qubit2bits(qc:QuantumCircuit):
    bits = None
    return bits


def process_quantum_communication(bits_Alice:list=None):
    print(f"bits_Alice = {bits_Alice}\n\n")

    # Erstellung des Circuits für Superdense Coded communication
    qc = get_entangled_qubits(2, len(bits_Alice))
    qc.barrier()#label="quantum circuit with entangled qubits")
    
    superdense_encode_bits2qubit(qc, bits_Alice)
    qc.barrier()#label="message bits superdense encoded")


    # 4. Send q0 via Quantum Channel to Bob


    # 5. Bob applies CNOT to q1 with q0 as a control qubit
    qc.cx(0, 1)

    # 6. Bob applies Hadamard to q0
    qc.h(0)

    # 7. Bob measures q0 and q1
    qc.measure(0, 1)
    qc.measure(1, 0)

    
    # visualize quantum circuit
    # qc.draw("mpl")
    print(qc)
    
    # Parameter zum Ausführen des Circuits im Simulator
    backend = Aer.get_backend("qasm_simulator")
    shots = 1024 # the number of shots in the experiment
        
    # Run the algorithm
    result = execute(qc, backend=backend, shots=shots).result()
    
    # Shows the results obtained from the quantum algorithm
    counts = result.get_counts()
    # visualization.plot_histogram(counts)
    
    print(f"\nThe measured outcomes of the circuits are: {counts}")
    
    bits_Bob = superdense_decode_qubit2bits(qc)
    print(f"bits_Bob = {bits_Bob}")
    
    

# --------------------------------------------------------------------------- #
# -------------------------------- M A I N ---------------------------------- #
# --------------------------------------------------------------------------- #

if "__main__" == __name__:


    RANDOM = False
    # Alices BitArray mit den zwei klassischen Bits via Verschränkung an Bob übertragen.
    if RANDOM:
        # Auswahl zufälliger Bits, die Alice senden möchte
        bits_Alice = [random.randint(0, 1), random.randint(0, 1)]
        process_quantum_communication(bits_Alice)
    else:
        for b1 in range(2):
            for b2 in range(2):
                process_quantum_communication([b1, b2])
                print("\n\n______________________________________\n")
