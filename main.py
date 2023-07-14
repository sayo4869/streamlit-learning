import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 入門")

st.write("DataFrame")

df = pd.DataFrame({"1列目": [1, 2, 3, 4], "2列目": [10, 20, 30, 40]})
st.table(df)

# markdownの表示
st.write("Markdown")
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

# プログレスバーの表示
st.write("progress bar")
"Start!"
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i + 1}")
    bar.progress(i + 1)
    time.sleep(0.2)
"Finish!"


# グラフの表示
st.write("graph")
left_column, right_column = st.columns(2)
df_chart = pd.DataFrame(np.random.rand(20, 3), columns=["a", "b", "c"])

left_column.table(df_chart)
right_column.line_chart(df_chart)
right_column.bar_chart(df_chart)

# 地図の表示
st.write("map")
df_map = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70], columns=["lat", "lon"]
)
st.map(df_map)

# 画像読み込み
st.write("Display Image")

if st.checkbox("Show image"):
    img = Image.open("sample.jpg")
    expander = st.expander("画像を開く")
    expander.image(img, caption="Ikuta Erika", use_column_width=True)

# select, text box
st.write("form sidebar")
st.sidebar.write("Interactive Widgets")
option = st.sidebar.selectbox("あなたが好きな数字を教えてください", list(range(1, 10)))
"あなたの好きな数字は", option, "です"

option = st.sidebar.text_input("あなたの趣味を教えてください。")
"あなたの趣味: ", option

condition = st.sidebar.slider("あなたの今の調子は?", 0, 100, 50)
"コンディション: ", condition
