# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 12:05:40 2024

    ┌────────────────────────────────┐
    │ Quantum Computing Helper Class │
    └────────────────────────────────┘
    
    
@history:
    2024-06-29:
        - initial upload of helpüer class QuantumHelper()
        - added method for superdense coding
        

@author: Florian Bethe
"""
from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, circuit_drawer, plot_histogram

class QuantumHelper():

    staticmethod
    def superdense_encode_bits2qubits(bits) -> QuantumCircuit:
        """
        Superdense encodes the given list of classical bits into qubits.
        Additionally it sets up a list of entangled qubits and returns a
        QuantumCircuit.
        The entagled qubits are added as this method is intended to be used for
        transmission of a message from a source to a target.
        
        TODO: Probably seperate steps into different atomic methods later.
        
        Parameters
        ----------
        bits : list, optional
    
        Returns
        -------
        qc : TYPE
            DESCRIPTION.
    
        """
        if 0 == len(bits):
            return QuantumCircuit()
        
        """
            Calculate the amount of needed qubits to superdense encode the
            amount of given bits.
            As we encode two classical bits into one qubit, we need the number
            of classical bits divided by two qubits. We have to add one further
            qubit for a uneven number of classical bits.
        """
        num_qubits = (len(bits) // 2) + (len(bits) % 2)
        
        # Initialise a QuantumCircuit with the number of qubits for sender and
        # recipient.
        qc = QuantumCircuit(2 * num_qubits)
        
        # Entangle the senders half of the quibits with the recipients half of 
        # quibits.
        for i in range(len(bits) // 2):  # go for the even even number of bits
            # apply hadamard-gate for each first (senders) qubit
            qc.h(i*2)  
            # apply CNOT-gate for each secong (recipients) qubit
            qc.cx(i*2, i*2+1)
        
        # firstly encode the even number of bits
        for i in range(0, len(bits) - (len(bits) % 2), 2):
            # take two bits into e separate list of bits to encode
            bit_pair = bits[i:i+2]
            
            # handle the four different possible options
            if bit_pair == [0, 0]:
                # keep the qubit in the initial hadamard state
                pass
            elif bit_pair == [0, 1]:
                # TODO: Add explanation
                qc.x(i+1)
            elif bit_pair == [1, 0]:
                # TODO: Add explanation
                qc.z(i+1)
            elif bit_pair == [1, 1]:
                # TODO: Add explanation
                qc.x(i+1)
                # TODO: Add explanation
                qc.z(i+1)
        
        # enconde the last bit, if number of bits are uneven
        if 0 != len(bits) % 2:
            last_bit_index = len(bits) - 1
            if bits[last_bit_index] == 1:
                # TODO: Add explanation
                qc.x(2 * num_qubits - 1)
        
        # measure all, to make it count
        qc.measure_all()
        
        return qc


# --------------------------------------------------------------------------- #
# -------------------------------- M A I N ---------------------------------- #
# --------------------------------------------------------------------------- #

if "__main__" == __name__:

    if True:
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
        
        
        def process_quantum_circuit(qc:QuantumCircuit):
            bits = None
        
            # Parameter zum Ausführen des Circuits im Simulator
            backend = Aer.get_backend("qasm_simulator")
            shots   = 1024 # the number of shots in the experiment
                
            # Run the algorithm
            result = execute(qc, backend=backend, shots=shots).result()
            
            # Shows the results obtained from the quantum algorithm
            counts = result.get_counts()
            plot_histogram(counts)
            
            print(f"\nThe measured outcomes of the circuits are: {counts}")
        
            return bits
        
        
        def superdense_decode_qubit2bits(qc:QuantumCircuit):
            # 6. Bob applies Hadamard to q0
            qc.h(0)
        
            # 7. Bob measures q0 and q1
            qc.measure(0, 1)
            qc.measure(1, 0)
        
        
            bits = process_quantum_circuit(qc)
        
        
            return bits


        def process_quantum_communication(bits_Alice:list=None):
            print(f"bits_Alice = {bits_Alice}\n\n")


            if False:        
                # Erstellung des Circuits für Superdense Coded communication
                qc = get_entangled_qubits(2, len(bits_Alice))
                qc.barrier()#label="quantum circuit with entangled qubits")
                
                superdense_encode_bits2qubit(qc, bits_Alice)
                qc.barrier()#label="message bits superdense encoded")
            
            
                # TODO: Clarify: 4. Send q0 via Quantum Channel to Bob
            
                # 5. Bob applies CNOT to q1 with q0 as a control qubit
                qc.cx(0, 1)
            

            else:
                qc = QuantumHelper.superdense_encode_bits2qubits(bits_Alice)
                # measure all, to make it count
                # qc.measure_all()

                # Parameter zum Ausführen des Circuits im Simulator
                backend = Aer.get_backend("qasm_simulator")
                shots   = 1024 # the number of shots in the experiment
                
                # Run the algorithm
                result = execute(qc, backend=backend, shots=shots).result()
                
                # Shows the results obtained from the quantum algorithm
                counts = result.get_counts()

                print(f"\nThe measured outcomes of the circuits are: {counts}")

        
            # visualize quantum circuit
            qc.draw("mpl")
            print(qc)
            
            
            # process circuit and decode superdense qubit2bits
            bits_Bob = superdense_decode_qubit2bits(qc)
            print(f"bits_Bob = {bits_Bob}")


        # Clear console
        #       https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
        #       https://hellocoding.de/blog/coding-language/python/farben-im-terminal
        import colorama
        colorama.init(autoreset=True)
        print("\033[H\033[J", end="")
        colorama.deinit()

        #   WARNINGS
        import warnings
        # Suppress or reset warings
        warnings.filterwarnings("ignore")
        # warnings.resetwarnings()


        RANDOM = False
        # Alices BitArray mit den zwei klassischen Bits via Verschränkung an Bob übertragen.
        if RANDOM:
            import random
            # Auswahl zufälliger Bits, die Alice senden möchte
            bits_Alice = [random.randint(0, 1), random.randint(0, 1)]
            process_quantum_communication(bits_Alice)
    
        else:
            for b1 in range(2):
                for b2 in range(2):
                    process_quantum_communication([b1, b2])
                    print("\n\n______________________________________\n")


    if False:
        # Erstellen eines QuantumCircuits mit zwei Qubits
        qc = QuantumCircuit(2)
        
        
        # Angenommen, die Basiszustände sind |0⟩ und |1⟩
        basis_state_0 = [1, 0]
        basis_state_1 = [0, 1]
        
        # Die zu kodierende Bitfolge ist 01
        message_bits = [0, 1]
        
        # Multiplizieren Sie jeden Bit mit dem entsprechenden Basiszustand
        for i, bit in enumerate(message_bits):
            if bit == 0:
                qc.append([qc.h], [i])
            else:
                qc.append([qc.x], [i])
        
        
        # Am Empfänger: Anwenden der inversen Operationen
        qc.append([qc.h, qc.x], [0])
        
        
        # Messung jedes Qubits
        qc.measure_all()
        
        
        
        
        
        
        
        
        # Beispielaufruf der Funktion mit einer ungeraden Anzahl von Bits
        bits_to_encode = [1, 0, 1, 1, 0]  # Eine Sequenz mit ungerader Bitanzahl
        qc = QuantumHelper.superdense_encode_bits2qubits(bits_to_encode)
        qc.draw(output='mpl')  # Zeichnet das Quantenkreisschema
        
        # Ausführung des Quantenkreises auf einem Simulator
        simulator = Aer.get_backend('qasm_simulator')
        job = execute(qc, simulator)
        result = job.result()
        
        # Ergebnisse anzeigen
        counts = result.get_counts(qc)
        print("\nErgebnisse:", counts)
    
    
