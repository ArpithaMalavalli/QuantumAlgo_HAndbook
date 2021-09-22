def bob_measure_qubit(bob_bases, qubit_index, qubit_circuit):
    ## WRITE YOUR CODE HERE
    if bob_bases[qubit_index]==0: # Z basis
        qubit_circuit.measure(0,0)
    else: #X basis so change first and measure
        qubit_circuit.h(0)
        qubit_circuit.measure(0,0)
        
    ## WRITE YOUR CODE HERE