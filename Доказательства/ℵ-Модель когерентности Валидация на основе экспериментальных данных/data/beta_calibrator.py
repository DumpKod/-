import numpy as np
from scipy.optimize import minimize

# Данные
empirical_data = {
    0.14: 150.0, 0.25: 120.0, 0.5: 90.0,
    0.8: 65.0, 1.0: 50.0, 1.2: 40.0
}
sigma2_noise = {
    0.14: 2.60e-2, 0.25: 5.03e-2, 0.5: 1.05e-1,
    0.8: 1.72e-1, 1.0: 2.16e-1, 1.2: 2.60e-1
}
ALPHA = 1.02e6
GAMMA0 = 45

def lambda_model(T, sigma_sq, beta):
    """Расчёт λ(T) с учётом шума"""
    return ALPHA * T + beta * sigma_sq + GAMMA0

def objective(beta, temps, T2_data, sigma2_data):
    """Функция ошибки для минимизации"""
    error = 0
    for T in temps:
        lambda_pred = lambda_model(T, sigma2_data[T], beta)
        lambda_emp = 1e6 / T2_data[T]  # Гц
        error += (lambda_pred - lambda_emp) ** 2
    return error

# Калибровка β
temps = list(empirical_data.keys())
result = minimize(objective, x0=0.0, args=(temps, empirical_data, sigma2_noise), method='Nelder-Mead')
beta_calibrated = result.x[0]
print(f"Откалиброванный β: {beta_calibrated:.2e}")

# Проверка λ(T)
lambda_values = {T: lambda_model(T, sigma2_noise[T], beta_calibrated) for T in temps}
t1e_values = {T: 1e6 / lam for T, lam in lambda_values.items()}
print("Предсказанные t₁/e (мкс):", t1e_values)