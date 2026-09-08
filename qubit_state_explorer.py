# Build a Qubit State Explorer
#
# Google Colab setup:
# Run this once in a Colab cell before running this script:
#
# !pip -q install qiskit qiskit-aer matplotlib pylatexenc

import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from IPython.display import display


# Qubit State Explorer

print("Available Gates")
print("1. X Gate")
print("2. Y Gate")
print("3. Z Gate")
print("4. H (Hadamard) Gate")
print("5. RY Gate")

choice_map = {
    "1": "X",
    "2": "Y",
    "3": "Z",
    "4": "H",
    "5": "RY",
    "X": "X",
    "Y": "Y",
    "Z": "Z",
    "H": "H",
    "RY": "RY",
}

while True:
    choice = input("\nChoose a gate: ").strip().upper()

    if choice in choice_map:
        gate = choice_map[choice]
        break

    print("Invalid choice. Please enter 1-5 or X, Y, Z, H, or RY.")


theta = None

if gate == "RY":
    while True:
        try:
            theta = float(
                input("Enter the rotation angle θ in radians: ").strip()
            )
            break
        except ValueError:
            print(
                "Invalid angle. Please enter a number, "
                "for example 0, 1.57, or 3.1416."
            )


print(f"\nSelected Gate: {gate}")

if theta is not None:
    print(f"θ = {theta:.6f} radians")


# Create a quantum circuit with 1 qubit
qc = QuantumCircuit(1)


# Apply the selected gate
if gate == "X":
    qc.x(0)

elif gate == "Y":
    qc.y(0)

elif gate == "Z":
    qc.z(0)

elif gate == "H":
    qc.h(0)

elif gate == "RY":
    qc.ry(theta, 0)


# Display the quantum circuit
print("\nQuantum Circuit")
display(qc.draw("mpl"))


# Calculate the final statevector
state = Statevector.from_instruction(qc)

print("\nFinal Statevector:")
print(state)


# Display the Bloch Sphere
print("\nBloch Sphere")
display(plot_bloch_multivector(state))


# Calculate measurement probabilities
probs = state.probabilities()

print("\nMeasurement Probabilities")
print(f"P(|0⟩) = {probs[0]:.4f}")
print(f"P(|1⟩) = {probs[1]:.4f}")


# Display a probability bar chart
plt.figure(figsize=(5, 3))
plt.bar(["|0⟩", "|1⟩"], probs)
plt.ylim(0, 1)
plt.ylabel("Probability")
plt.title(f"Measurement Probabilities — {gate} Gate")
plt.show()
