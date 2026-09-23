import json
import matplotlib.pyplot as plt

head_x, head_y, head_z = [], [], []
file_name = 'trackingData_20260505_165740.txt'

# 1. Читаем и парсим данные
with open(file_name, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip(): continue
        try:
            data = json.loads(line)
            if "Head" in data and "pose" in data["Head"]:
                parts = data["Head"]["pose"].split(',')
                # Склеиваем дроби, исправляя баг с запятыми
                hx = float(f"{parts[0]}.{parts[1]}")
                hy = float(f"{parts[2]}.{parts[3]}")
                hz = float(f"{parts[4]}.{parts[5]}")
                
                head_x.append(hx)
                head_y.append(hy)
                head_z.append(hz)
        except:
            pass

# Убираем стартовый шум (первые 50 фреймов)
head_x = head_x[50:]
head_y = head_y[50:]
head_z = head_z[50:]

frames = range(len(head_x))

# 2. Строим строгие аналитические графики
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
fig.suptitle('Анализ смещения шлема (Head Tracking) по осям', fontsize=14)

ax1.plot(frames, head_x, color='red')
ax1.set_ylabel('Ось X (Вправо-Влево)')
ax1.grid(True)

ax2.plot(frames, head_y, color='green')
ax2.set_ylabel('Ось Y (Вверх-Вниз)')
ax2.grid(True)

ax3.plot(frames, head_z, color='blue')
ax3.set_ylabel('Ось Z (Вперед-Назад)')
ax3.set_xlabel('Фреймы (Время)')
ax3.grid(True)

plt.tight_layout()
plt.show()