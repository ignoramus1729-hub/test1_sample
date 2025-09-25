
# 간단한 데이터 시각화 예시 (선 그래프)

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]


import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 경로 지정

import os

font_path = os.path.join(os.path.dirname(__file__), '../fonts/NanumGothic-Regular.ttf')
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
font_prop = font_manager.FontProperties(fname=font_path)

st.title('간단한 선 그래프 예시')
st.write('아래는 임의의 데이터를 시각화한 선 그래프입니다.')

fig, ax = plt.subplots()
ax.plot(x, y, marker='o')
ax.set_xlabel('X축', fontproperties=font_prop)
ax.set_ylabel('Y축', fontproperties=font_prop)
ax.set_title('간단한 선 그래프 예시', fontproperties=font_prop)
ax.grid(True)
st.pyplot(fig)
