import math

# Данные задачи
N1, E1, N2, E2 = 1367.14, 2012.57, 2253.86, 3009.35
mN1, mE1, mN2, mE2 = 0.06, 0.07, 0.08, 0.09

# Разности координат
dN, dE = N2 - N1, E2 - E1
denominator = dE**2 + dN**2

# Частные производные
d_theta_dN1 = -dE / denominator
d_theta_dE1 = dN / denominator
d_theta_dN2 = dE / denominator
d_theta_dE2 = -dN / denominator

# Средняя квадратическая погрешность
m_theta = math.sqrt(
    (d_theta_dN1 * mN1)**2 +
    (d_theta_dE1 * mE1)**2 +
    (d_theta_dN2 * mN2)**2 +
    (d_theta_dE2 * mE2)**2
)

# Дирекционный угол (в радианах)
theta = math.atan2(dN, dE)

# Результаты
print(f"Дирекционный угол (в радианах): {theta:.6f}")
print(f"Средняя квадратическая погрешность угла (в радианах): {m_theta:.6f}")