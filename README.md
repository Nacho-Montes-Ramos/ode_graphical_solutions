# Differential Equations in Physics with Python

This repository contains a single Python script/Notebook where I explore several classical problems in physics by solving and visualizing their differential equations.

## Overview

The code is divided into four main parts:

1. **Damped Driven Pendulum**
2. **Quantum Harmonic Oscillator (Schrödinger Equation)**
3. **Two Coupled Oscillators**
4. **Gravitational Motion: Earth & Halley's Comet**

---

## 1. Damped Driven Pendulum

In the first part, I solve and plot the differential equation of a **damped driven pendulum**.  

- I set up the equation of motion including the damping term and the external driving force.  
- The solution is obtained numerically and the angular position as a function of time is plotted.  
- This section illustrates how the behavior changes with different parameters (damping, driving amplitude and frequency).

---

## 2. Quantum Harmonic Oscillator (Schrödinger Equation)

The second part focuses on the **time-independent Schrödinger equation** for the **quantum harmonic oscillator**.

- First, I use the **Hermite polynomials** provided by `scipy` to construct the analytical wavefunctions.
- Then, I also solve the corresponding differential equation numerically to obtain the same eigenstates.
- Finally, I plot the wavefunctions and compare the results.

This section connects numerical methods with well-known analytical solutions in quantum mechanics.

---

## 3. Two Coupled Oscillators

In the third part, I study a system of **two coupled oscillators**.

- I write the coupled second-order differential equations describing the motion.  
- The system is solved numerically and I plot:
  - The positions of both oscillators as a function of time.
  - Their velocities as a function of time.

This illustrates normal modes and energy exchange between coupled degrees of freedom.

---

## 4. Gravitational Motion: Earth & Halley's Comet

The last part of the code deals with **gravitational orbits**.

- I solve the differential equations corresponding to Newtonian gravity for two bodies: the **Earth** and **Halley's Comet**.
- Using the numerical solutions, I plot:
  - \( x(t) \) and \( y(t) \) for both bodies.
  - The phase-space trajectory \( x(y) \).
  - The velocity \( v(t) \).

This section shows how orbital motion and very different time/length scales (Earth vs Halley) can be described with the same gravitational law.

---

## Requirements

The code uses:

- Python 3
- `numpy`
- `scipy`
- `matplotlib`

You can install the required packages with:

```bash
pip install numpy scipy matplotlib
