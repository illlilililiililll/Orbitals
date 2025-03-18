import numpy as np
import plotly.graph_objects as go
from Orbital import Orbital, R, Y

a0 = 1.0
Z = 1.0

def psi(orbital: Orbital, x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(np.divide(z, r, out=np.zeros_like(r), where=r != 0))
    phi = np.arctan2(y, x)
    return orbital.r(r, a0, Z) * orbital.y(theta, phi)

def plot(orbital: Orbital, N=150, range_val=20, threshold=0.00001):
    """
    Orbital: Wave function (ψ) combining radial (R) and angular (Y) parts.
    N: Number of points per axis.
    range_val: Range for the plot (must be > 0).
    threshold: Probability density threshold for visualization.
    """
    # Create a grid of points.
    x = np.linspace(-range_val, range_val, N)
    y = np.linspace(-range_val, range_val, N)
    z = np.linspace(-range_val, range_val, N)
    X, Y, Z = np.meshgrid(x, y, z)

    # Compute wavefunction and probability density.
    psi_vals = psi(orbital, X, Y, Z)
    prob_density = psi_vals**2

    # Create a mask for points with significant probability density.
    mask = prob_density > threshold

    # Masked coordinates and wavefunction values.
    X_masked = X[mask]
    Y_masked = Y[mask]
    Z_masked = Z[mask]
    psi_masked = psi_vals[mask]

    # Compute phase and normalize it to [0, 1] for the alpha channel.
    phase = np.angle(psi_vals)
    norm_phase = ((phase + np.pi) / (2 * np.pi))[mask]
    alpha_values = norm_phase  # Already between 0 and 1

    # Build color strings. Use blue (0,0,255) if psi >= 0, red (255,0,0) if psi < 0.
    colors = []
    for psi_val, a in zip(psi_masked, alpha_values):
        if psi_val.real >= 0:
            colors.append(f"rgba(0,0,255,{a})")
        else:
            colors.append(f"rgba(255,0,0,{a})")

    # Create the 3D scatter plot using Plotly.
    fig = go.Figure(data=[go.Scatter3d(
        x=X_masked,
        y=Y_masked,
        z=Z_masked,
        mode='markers',
        marker=dict(
            size=3,
            color=colors
        )
    )])
    fig.update_layout(
        
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title="Z"
        ),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    return fig
