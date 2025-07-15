import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

plt.rcParams['font.family'] = 'DejaVu Sans'

ALPHA = 1.02e6
BETA = 1.5e6
GAMMA0 = 45
PHI_N = 0.021

empirical_data = {
    0.14: 150.0, 0.25: 120.0, 0.5: 90.0,
    0.8: 65.0, 1.0: 50.0, 1.2: 40.0
}
sigma2_noise = {
    0.14: 0.026, 0.25: 0.0503, 0.5: 0.105,
    0.8: 0.172, 1.0: 0.216, 1.2: 0.26
}

def lambda_model(T, sigma_sq, beta=BETA):
    return ALPHA * T + beta * sigma_sq + GAMMA0

t_us = np.linspace(0, 300, 500)
t_s = t_us * 1e-6

plt.figure(figsize=(12, 8))

for i, (temp, T2_emp) in enumerate(empirical_data.items()):
    lam_simple = 1e6 / T2_emp
    lam_full = lambda_model(temp, sigma2_noise[temp])
    T_simple = np.exp(-lam_simple * t_s)
    T_full = (1 - PHI_N) * np.exp(-lam_full * t_s)
    color = plt.cm.viridis(i / 5)
    plt.plot(t_us, T_simple, color=color, ls='--', 
             label=f'{temp}K упрощ. (T₂={T2_emp:.1f} мкс)')
    plt.plot(t_us, T_full, color=color, ls='-', 
             label=f'{temp}K полная (t₁/e={1e6/lam_full:.2f} мкс)')
    plt.scatter(T2_emp, np.exp(-1), color=color, s=80, zorder=5)
    plt.scatter(1e6 / lam_full, (1 - PHI_N) * np.exp(-1), color=color, s=80, marker='s')
    plt.axvline(T2_emp, color='gray', ls=':', alpha=0.7)

plt.title('Верификация Aleph-модели когерентности', fontsize=14)
plt.xlabel('Время (мкс)', fontsize=12)
plt.ylabel('T(t)', fontsize=12)
plt.yscale('linear')
plt.ylim(0, 1.05)
plt.xlim(0, 300)
plt.grid(alpha=0.3)
plt.legend(loc='upper right')
plt.text(250, 0.9, f"λ(T) = {ALPHA/1e6:.2f}×10⁶·T + {BETA:.2e}·σ²_noise + {GAMMA0}", 
         fontsize=10, bbox=dict(alpha=0.2))
plt.text(250, 0.8, f"|¬φⁿ| = {PHI_N}", fontsize=10)

plt.savefig('coherence_validation_plot_corrected.svg', format='svg', bbox_inches='tight')
plt.show()