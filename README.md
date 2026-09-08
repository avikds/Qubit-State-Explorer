# Qubit State Explorer

## Overview

`Qubit_State_Explorer.ipynb` implements a single-qubit state exploration program in Qiskit. The qubit is initialized in the computational basis state

$$
|0\rangle =
\begin{bmatrix}
1\\
0
\end{bmatrix},
$$

and the user selects one gate from the following set:

- Pauli-X (`X`)
- Pauli-Y (`Y`)
- Pauli-Z (`Z`)
- Hadamard (`H`)
- Y-axis rotation (`RY`)

For the `RY` gate, the program requests a rotation angle $\theta$ in radians.

After the gate is applied, the notebook reports the resulting state in three complementary forms:

1. the quantum circuit,
2. the single-qubit Bloch-sphere representation, and
3. the computational-basis measurement probabilities $P(0)$ and $P(1)$.

The notebook evaluates the state with Qiskit's statevector formalism before any measurement is introduced. This preserves the quantum state required for Bloch-sphere visualization and allows the computational-basis probabilities to be obtained directly from the state amplitudes.

## Scientific Basis

A general pure state of one qubit can be written as

$$
|\psi\rangle = \alpha |0\rangle + \beta |1\rangle,
$$

where the amplitudes satisfy

$$
|\alpha|^2 + |\beta|^2 = 1.
$$

When the qubit is measured in the computational basis, the Born rule gives

$$
P(0)=|\alpha|^2,
\qquad
P(1)=|\beta|^2.
$$

For a pure single-qubit state, the Bloch-vector representation provides an equivalent geometric description of the state. For amplitudes $\alpha$ and $\beta$, the Cartesian Bloch components are

$$
x = 2\operatorname{Re}(\alpha^*\beta),
$$

$$
y = 2\operatorname{Im}(\alpha^*\beta),
$$

$$
z = |\alpha|^2-|\beta|^2.
$$

The Bloch vector therefore identifies the location of the state on the unit sphere while the measurement probabilities describe the same state with respect to the computational basis.

## Quantum Gates Used

### Pauli-X Gate

The X gate is

$$
X =
\begin{bmatrix}
0 & 1\\
1 & 0
\end{bmatrix}.
$$

Applied to the initial state $|0\rangle$,

$$
X|0\rangle = |1\rangle.
$$

Thus, an X operation exchanges the computational-basis states.

### Pauli-Y Gate

The Y gate is

$$
Y =
\begin{bmatrix}
0 & -i\\
i & 0
\end{bmatrix}.
$$

Applied to $|0\rangle$,

$$
Y|0\rangle = i|1\rangle.
$$

The factor $i$ changes the phase of the amplitude, but it does not change the probability of measuring $|1\rangle$.

### Pauli-Z Gate

The Z gate is

$$
Z =
\begin{bmatrix}
1 & 0\\
0 & -1
\end{bmatrix}.
$$

Applied to $|0\rangle$,

$$
Z|0\rangle = |0\rangle.
$$

For the initial computational-basis state, the Z operation therefore leaves the measurement probabilities unchanged.

### Hadamard Gate

The Hadamard operator is

$$
H=
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1\\
1 & -1
\end{bmatrix}.
$$

Its action on $|0\rangle$ is

$$
H|0\rangle
=
\frac{|0\rangle+|1\rangle}{\sqrt{2}}.
$$

Consequently,

$$
P(0)=P(1)=\frac{1}{2}.
$$

The Hadamard gate moves the initial state from the north pole of the Bloch sphere to the positive x-axis.

### RY Gate

The notebook uses Qiskit's `ry(theta, 0)` operation, corresponding to the matrix

$$
R_y(\theta)
=
\begin{bmatrix}
\cos(\theta/2) & -\sin(\theta/2)\\
\sin(\theta/2) & \cos(\theta/2)
\end{bmatrix}.
$$

For the initial state $|0\rangle$,

$$
R_y(\theta)|0\rangle
=
\cos\left(\frac{\theta}{2}\right)|0\rangle
+
\sin\left(\frac{\theta}{2}\right)|1\rangle.
$$

Therefore,

$$
P(0)=\cos^2\left(\frac{\theta}{2}\right),
\qquad
P(1)=\sin^2\left(\frac{\theta}{2}\right).
$$

For this particular real-amplitude state, the Bloch coordinates are

$$
(x,y,z)=(\sin\theta,\,0,\,\cos\theta).
$$

This makes the RY gate especially useful for observing continuous state rotations and the corresponding continuous change in computational-basis probabilities.

## Notebook Structure

The executed notebook is organized into the following stages.

### 1. Dependency Installation

The notebook installs the packages required for the Qiskit workflow and visualization:

```python
!pip -q install qiskit qiskit-aer matplotlib pylatexenc
```

`pylatexenc` is included so that Qiskit's Matplotlib circuit drawer can render circuit diagrams in the Colab environment.

### 2. Imports

The implementation imports:

```python
import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from IPython.display import display
```

The central objects are `QuantumCircuit` for circuit construction, `Statevector` for exact state evolution, and `plot_bloch_multivector` for geometric visualization.

### 3. Interactive Gate Selection

The user is presented with five choices:

```text
1. X Gate
2. Y Gate
3. Z Gate
4. H (Hadamard) Gate
5. RY Gate
```

Both numeric and gate-name input are accepted. Invalid choices trigger another prompt.

When `RY` is selected, a second input requests the rotation angle $\theta$ in radians. The input is converted to a floating-point value and is validated so that non-numeric input does not terminate the program.

### 4. Circuit Construction

A single-qubit circuit is created:

```python
qc = QuantumCircuit(1)
```

The selected operation is then applied to qubit `0`. The circuit is displayed with:

```python
display(qc.draw("mpl"))
```

No classical register or measurement operation is inserted into this circuit. This is intentional: the notebook first inspects the coherent quantum state and only computes measurement probabilities from that state.

### 5. Final Statevector

The post-gate state is calculated with:

```python
state = Statevector.from_instruction(qc)
```

The statevector contains the complex probability amplitudes associated with the computational-basis states $|0\rangle$ and $|1\rangle$.

### 6. Bloch-Sphere Visualization

The statevector is passed to:

```python
plot_bloch_multivector(state)
```

For one qubit, the resulting Bloch sphere provides a geometric representation of the final pure state.

### 7. Measurement Probabilities

The notebook obtains the exact computational-basis probabilities from:

```python
probs = state.probabilities()
```

and reports

```python
P(|0⟩)
P(|1⟩)
```

It also generates a bar chart for the two probabilities.

## Executed Result in This Notebook

The saved execution corresponds to the following interactive input:

```text
Choose a gate: RY
Enter the rotation angle θ in radians: 45
```

Thus,

$$
\theta = 45 \text{ radians}.
$$

The resulting statevector stored in the executed notebook is

```text
Statevector([-0.87330464+0.j, -0.48717451+0.j],
            dims=(2,))
```

The amplitudes are therefore approximately

$$
\alpha=-0.87330464,
\qquad
\beta=-0.48717451.
$$

The associated computational-basis probabilities are

$$
P(0)=|\alpha|^2\approx0.762661,
$$

$$
P(1)=|\beta|^2\approx0.237339.
$$

The notebook displays these values rounded to four decimal places:

```text
P(|0⟩) = 0.7627
P(|1⟩) = 0.2373
```

The corresponding Bloch coordinates are

$$
x=\sin(45)\approx0.850904,
$$

$$
y=0,
$$

$$
z=\cos(45)\approx0.525322.
$$

The signs of both state amplitudes are negative in the stored statevector. Because both amplitudes share the same overall phase, this does not change the physical quantum state or its measurement probabilities.

## Implementation Notes

### Statevector Rather Than Sampled Counts

The notebook calculates measurement probabilities directly from the statevector rather than estimating them from a finite number of simulator shots. This produces the exact probabilities of the ideal circuit state within the statevector simulator.

For example, for the `RY` operation,

$$
|\psi\rangle
=
\cos\left(\frac{\theta}{2}\right)|0\rangle
+
\sin\left(\frac{\theta}{2}\right)|1\rangle,
$$

so the computational-basis probabilities follow directly from the squared magnitudes of these amplitudes.

### Measurement Is Not Added to the Circuit

The circuit itself contains only the selected gate. The notebook does not append `measure()` before creating the statevector. A projective measurement would collapse the state and would no longer represent the pre-measurement state required for the Bloch-sphere plot.

The probability calculation is therefore performed mathematically from the final statevector.

### Input Handling

The gate-selection logic accepts either numeric menu entries or the corresponding gate names. The RY angle is parsed with `float()` and repeatedly requested until a valid numerical value is entered.

## Requirements

The notebook is intended for execution in **Google Colab** with Python 3.

The main dependencies are:

- Python 3
- Qiskit
- Qiskit Aer
- Matplotlib
- `pylatexenc`

The notebook installs these packages in its first executable cell, so a separate environment setup is not required for a standard Colab session.

## Running the Notebook

Open `Qubit_State_Explorer_Final_Notebook.ipynb` in Google Colab and run the cells from top to bottom.

When the interactive cell executes:

1. Select `X`, `Y`, `Z`, `H`, or `RY`, or enter the corresponding menu number.
2. For `RY`, enter the rotation angle in radians.
3. The notebook displays the resulting circuit.
4. The exact final statevector is printed.
5. The final state is shown on the Bloch sphere.
6. The probabilities of measuring `|0⟩` and `|1⟩` are printed and plotted.

A useful set of test cases is:

```text
X
Y
Z
H
RY with θ = 0
RY with θ = π/2
RY with θ = π
```

These cases expose the basic behavior of the implemented gates and, for `RY`, illustrate continuous rotation from one computational-basis state toward the other.

## Repository Contents

The principal repository artifact is:

```text
Qubit_State_Explorer.ipynb
```

This notebook contains the executable implementation, explanatory markdown, circuit visualization, Bloch-sphere output, and probability visualization.
