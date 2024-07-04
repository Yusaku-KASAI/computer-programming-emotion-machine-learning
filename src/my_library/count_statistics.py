#入力された文章 sent に含まれる単語を感情辞書 dic と照合し、各感情（ポジティブ、ネガティブ、ニュートラル）の単語数をカウントしてベクトルとして返す関数です。
from janome.tokenizer import Tokenizer

NEGATIVE = "n"
POSITIVE = "p"
NEUTRAL = "e"

def count_and_vectorize(dic, sent):
    tokenizer = Tokenizer()
    num_positive = 0
    num_negative = 0
    num_neutral = 0
    words = []
    for token in tokenizer.tokenize(sent):
        words.append(token.base_form)

    # 辞書を単語をキーとして検索
    for word in words:
        if word in dic:
            emotion = dic[word]
            if emotion == NEGATIVE:
                num_negative += 1
            elif emotion == POSITIVE:
                num_positive += 1
            elif emotion == NEUTRAL:
                num_neutral += 1

    num_total = num_negative + num_positive + num_neutral 
    
    return [num_positive, num_negative, num_neutral, num_total]