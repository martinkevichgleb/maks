import math

tg = math.tan

H1, mH1 = 114.427, 0.008  # Отметка H1 и её погрешность
H2, mH2 = 118.583, 0.007  # Отметка H2 и её погрешность
D, mD = 186.54, 0.08      # Наклонная длина и её погрешность

dH = H2 - H1 # Разность отметок

alpha = math.atan(dH / D) # Угол наклона (в радианах)

# Частные производные
tg2_alpha = (dH / D) ** 2  # tg^2(alpha) 
denominator = D * (1 + tg2_alpha)

d_alpha_dH1 = -1 / denominator
d_alpha_dH2 = 1 / denominator
d_alpha_dD = -dH / (D**2 * (1 + tg2_alpha))

# Средняя квадратическая погрешность угла (в радианах)
m_alpha_rad = math.sqrt(
    (d_alpha_dH1 * mH1)**2 +
    (d_alpha_dH2 * mH2)**2 +
    (d_alpha_dD * mD)**2
)

m_alpha_sec = m_alpha_rad * (180 * 3600) / math.pi # Перевод погрешности в секунды

##Ответ
print(f"Угол наклона линии (в радианах): {alpha:.6f}")
print(f"Средняя квадратическая погрешность угла (в радианах): {m_alpha_rad:.10f}")
print(f"Средняя квадратическая погрешность угла (в секундах): {m_alpha_sec:.2f}")