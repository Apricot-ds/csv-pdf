import streamlit as st
import numpy as np

st.title('CSVファイルをPDFファイルにして保存')

sentence1 ='Pythonを使ってCSVファイルをPDFにして保存する方法を記述する.'
sentence2 = 'PythonのPDF生成ライブラリ "reportlab" をinstall\n '
sentence3 = 'ttfフォントのイメージをダウンロード（ipaexm.ttfを使用）'
sentence4 = 'ソースコード例．sample.csvをdataframeにしたものをoutput.pdfと出力\n（途中の過程でdataframeのtableサイズを取得するため，provisional.pdfを生成）'

st.text(sentence1)
st.subheader('準備1')
st.text(sentence2)
st.code('pip install reportlab')

st.subheader('準備2')
st.text(sentence3)
st.link_button("リンク", "https://moji.or.jp/ipafont/ipaex00401/")

st.subheader('サンプルコード')
st.text(sentence4)
code = '''
from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
import pandas as pd
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# CSVファイルを読み込む
df = pd.read_csv('sample.csv')

# カスタムページサイズを定義（幅: 30ピクセル、高さ: 30ピクセル）
custom_page_size_1 = (30, 30)

# PDFファイルを作成し、カスタムページサイズで設定
provisional_pdf = canvas.Canvas('provisional.pdf', pagesize=landscape(custom_page_size_1))

# 日本語フォントの設定
font_path = 'ipaexm.ttf'  # インストールしたフォントのパスを指定
pdfmetrics.registerFont(TTFont('JapaneseFont', font_path))

# DataFrameをTableオブジェクトに変換
data = [df.columns.values.tolist()] + df.values.tolist()
table = Table(data)

# テーブルスタイルの設定
style = TableStyle([
    ('GRID', (0, 0), (-1, -1), 0.1, colors.black),  # 枠線を追加
    ('FONTNAME', (0, 0), (-1, -1), 'JapaneseFont'),  # フォントを設定
    ('FONTSIZE', (0, 0), (-1, -1), 10),  # フォントサイズを設定
])
table.setStyle(style)

# テーブルの幅と高さを計算
width, height = table.wrapOn(provisional_pdf, 0, 0)  # 幅と高さを指定してテーブルを描画

# テーブルを描画してPDFファイルに追加
table.drawOn(provisional_pdf, 0, 0)  # 位置を調整してテーブルを描画

# PDFファイルを保存
provisional_pdf.save()

# テーブルの幅と高さを出力
# print('テーブルの幅:', width)
# print('テーブルの高さ:', height)

custom_page_size = (width+40, height+40)
# PDFファイルを作成し、カスタムページサイズで設定
c = canvas.Canvas('output.pdf', pagesize=landscape(custom_page_size))

# テーブルを再度作成
table = Table(data)
table.setStyle(style)

# テーブルの幅と高さを計算
width, height = table.wrapOn(c, 0, 0)  # 幅と高さを指定してテーブルを描画

# テーブルを描画してPDFファイルに追加
table.drawOn(c, 20, 20)  # 位置を調整してテーブルを描画

# PDFファイルを保存
c.save()
'''
st.code(code, language='python')
