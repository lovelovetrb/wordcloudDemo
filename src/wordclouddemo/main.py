from wordcloud import WordCloud
import MeCab
from glob import glob
from matplotlib import pyplot as plt

 #WordCloud #文書を読み込み・邪魔になる記号を除去
filepaths = glob('socrates.txt')
font_path = "/usr/share/fonts/TTF/KleeOne-Regular.ttf"
filepaths = filepaths[0]
with open(filepaths, "r", encoding="utf8") as f:
    txt = f.read().replace('\u3000', '')

#WordCouldを作成 - Mecabで形態素解析し、名詞のみを抽出する
wc = WordCloud( width =1920, height = 1080, font_path = font_path)
mecab = MeCab.Tagger()
nodes = mecab.parseToNode(txt)
s = []

while nodes:
    if nodes.feature[:2] == '名詞':
        s.append(nodes.surface)
    nodes = nodes.next

#ストップワードを設定　→ ストップワードを除去してWordCloudを出力
stopwords = {"もの","これ","ため","それ","ところ","よう","こと"}
wc = WordCloud(width =1920, height = 1080, stopwords=stopwords, font_path = font_path, colormap = "PuBu")

wc.generate(" ".join(s))
wc.to_file('socrates_jp02.png')
plt.imshow(wc)
