from tkinter import Button
from turtle import right
import streamlit as st
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('DataFrame')


latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)



# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')

# expander = st.expander('問い合わせ')
# expander.write('内容')
# expander.write('内容')
# expander.write('内容')
# expander.write('内容')



# img = Image.open('背景画像.png')

# st.image(img)


# df = pd.DataFrame({
#     '1列目' : [1,2,3,4,],
#     '2列目' : [10,20,30,40]
# })

# aa = pd.DataFrame(
#     np.random.rand(100,2)/[20] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# option = st.selectbox(
#     'あなたの好きな数字を入れてください',
#     list(range(1,11))
# )

# test = st.text_input('あなたの趣味は何ですか？')
# 'あなたの趣味:' ,test

# condition = st.slider('あなたの調子を教えてください' ,0,100,50)

# condition 





# if st.checkbox('show image'):
#     img = Image.open('背景画像.png')
#     st.image(img, caption='a,' , use_column_width=True)



# st.write(df)

# st.table(df.style.highlight_max(axis=1))




# st.write(aa)
# st.map(aa)

    
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ``` 

# """