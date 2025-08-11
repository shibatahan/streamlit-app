import streamlit as st
from PIL import Image
import pandas as pd

st.title('アプリ')
st.caption('説明文')
st.subheader('自己紹介')
st.text('コメント')

# コード表示
code = '''
import streamlit as st

st.title('アプリ')
'''
st.code(code, language='python')

# 画像表示
image = Image.open('sample.jpg')
st.image(image, width=200)

with st.form(key='profile_form'):

#テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')

#セレクトボックス
    age_category = st.radio(
        '年齢層',
        ('子供(18歳未満)','大人(18歳以上)')
    )
    #複数選択
    hobby = st.multiselect(
        '趣味',
        ('スポーツ','読書','釣り','ゲーム')
    )
    #選択肢を定義しセレクトボックスで選択
    effort_values = [0, 4] + list(range(12, 257, 8))  # 12〜256まで8刻み
    height = st.selectbox('努力値', effort_values)
    
    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    st.text(f'趣味: {",".join(hobby)}')


if submit_btn:
    st.text(f'ようこそ{name}さん。{address}に書籍を送りました')
    st.text(f'年齢層: {age_category}')

#データ分析関連
df = pd.read_csv('pokeapi250724.csv',index_col='英語名')
st.dataframe(df)


