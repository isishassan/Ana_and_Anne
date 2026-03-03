import numpy as np
import matplotlib.pyplot as plt

def plot_sine(amplitude=1.0, frequency=1.0, phase=0.0, duration=2*np.pi, points=1000):
    """
    Plot a simple sinusoidal (sine) wave.
    """
    x = np.linspace(0, duration, points)
    y = amplitude * np.sin(frequency * x + phase)

    plt.figure()
    plt.plot(x, y)
    plt.title("Sine Wave")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.grid(True)
    plt.show()


from src.viz import plot_sine

plot_sine(amplitude=1.0, frequency=2.0, phase=0.0)