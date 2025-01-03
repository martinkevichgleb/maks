import math

# Исходные данные
h = 0.5  # высота сечения, м
m_h = 0.1  # погрешность высоты сечения, м
l = 2.4  # расстояние от горизонтали, см
m_l = 0.1  # погрешность расстояния, см
d = 5.7  # заложение, см
m_d = 0.2  # погрешность заложения, см

# Вычисление высоты H
H = h * (l / d)

# Частные производные
dH_dl = h / d  # по l
dH_dd = -h * l / (d ** 2)  # по d
dH_dh = l / d  # по h

# Средняя квадратическая погрешность
m_H = math.sqrt(
    (dH_dl * m_l) ** 2 +
    (dH_dd * m_d) ** 2 +
    (dH_dh * m_h) ** 2
)

# Перевод в см
m_H *= 100  # из метров в сантиметры

# Вывод результатов
print(f"Средняя квадратическая погрешность (m_H): {m_H:.2f} см")
