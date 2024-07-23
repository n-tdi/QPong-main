"""
Constants and utilities for quantum states
"""

MAX_NUM_QUBITS = 10


def comp_basis_states(num_qubits):
    """
    Get computational basis states for a quantum state with
    a specified number of qubits
    """
    num_qb = min(num_qubits, MAX_NUM_QUBITS)
    basis_states = []
    for idx in range(2**num_qb):
        state = format(idx, "0" + str(num_qb) + "b")
        basis_states.append(state)
    return basis_states
