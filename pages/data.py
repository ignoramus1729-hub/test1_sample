
# 간단한 데이터 시각화 예시 (선 그래프)

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 경로 지정
font_path = "./fonts/NanumGothic-Regular.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, marker='o')
plt.title('간단한 선 그래프 예시')
plt.xlabel('X축')
plt.ylabel('Y축')
plt.grid(True)
plt.show()
