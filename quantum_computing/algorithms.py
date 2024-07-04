# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 10:16:48 2024

@author: Florian Bethe
"""

###############################################################################
## libraries
"""
    qiskit              0.46.0
    qiskit-aer          0.14.2
    qiskit-ibm-runtime  0.23.0
    qiskit-terra        0.46.0
"""
from qiskit import QuantumCircuit, Aer, execute, visualization


###############################################################################
## Superdense Coding
"""
    Superdense Coding Protocol

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
"""
if False:
    for b1 in range(2):
        for b2 in range(2):

            bits_Alice = [b1, b2]
            print(f"bits_Alice = {bits_Alice}\n\n")
        
            # Erstellung des Circuits für Superdense Coded communication
            qc = QuantumCircuit(2, len(bits_Alice))
            # The Hadamard gate equalizes the odds for each value of this qubit
            qc.h(0)
            # entanglement by controlled not gatter
            qc.cx(0, 1)
            qc.barrier()#label="quantum circuit with entangled qubits")
            
            if 1 == bits_Alice[0]:
                # 2. If 1st bit is 1 apply phase flip to q0 (qc.z())
                #    - If 1st bit is 0 q0 remains unchanged
                qc.z(0)
                
            if 1 == bits_Alice[1]:
                # 3. If 2nd bit is 1 apply NOT gate to q0 (qc.x())
                #     - If 2nd bit is 0 q0 remains unchanged
                qc.x(0)
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
            visualization.plot_histogram(counts)
            
            print(f"\nThe measured outcomes of thh circuits are: {counts}")
            
            # bits_Bob = superdense_decode_qubit2bits(qc)
            # print(f"bits_Alice = {bits_Bob}")

            print("\n\n\n______________________________________")


###############################################################################
## Teleportation
"""
    Teleportation Protocol
    
        We start with 3 qubits q0, q1, q2
        Alice wants to teleport q0 to Bob
        
        1.  Alice and Bob entangle q1 and q2

        2.  Alice takes q0 an q1,
            Bob takes q2

        3.  Alice applies CNOT to q1 with q0 as a control qubit

        4.  Alice applies Hadamard to q0

        5.  Alice measures both q0 and q1 
            and sends 2 classical bits to Bob

        6.  Bob applies CNOT to his qubit q2 with q1 as a control qubit

        7.  Bob applies C-phase-flip to q2 with q0 as control qubit
"""
if False:
    # 0. leeren Quantenschaltkreis mit 3 Qubits und 3 klassischen Bits erstellen
    qc = QuantumCircuit(3, 3) # 1. Anzahl Quantenbits, 2. Anzahl klassische Bits
    
    # 1. Alice and Bob entangle q1 and q2
    qc.x(0)
    
    qc.barrier()
    
    qc.h(1)
    qc.cx(1, 2)
    
    qc.barrier()
    
    # 2. Alice takes q0 and q1, Bob takes q2
    # Dies ist implizit durch die folgenden Operationen gegeben
    
    # 3. Alice applies CNOT to q1 with q0 as a control qubit
    qc.cx(0, 1)
    
    
    # 4. Alice applies Hadamard to q0
    qc.h(0)
    
    qc.barrier()
    
    # 5. Alice measures both q0 and q1 and sends 2 classical bits to Bob
    if True:
        qc.measure([0, 1], [0, 1])
    else:
        qc.measure(0, 0)
        qc.measure(1, 1)
    
    qc.barrier()
    
    # 6. Bob applies CNOT to his qubit q2 with q1 as a control qubit
    qc.cx(1, 2)
    
    
    # 7. Bob applies C-phase-flip to q2 with q0 as control qubit
    qc.cz(0, 2)
    qc.measure(2, 2)
       
    print(qc)
    qc.draw("mpl")
    
    
    backend = Aer.get_backend("qasm_simulator")
    # shots = 1024 # the number of shots in the experiment
    
    # Run the algorithm
    result = execute(qc, backend=backend).result()
    # result = execute(qc, backend=backend, shots=shots).result()
    
    # Shows the results obtained from the quantum algorithm
    counts = result.get_counts()
    visualization.plot_histogram(counts)
    print(f"\nThe measured outcomes of the circuits are: {counts}")


###############################################################################
## Shore Algorithm
