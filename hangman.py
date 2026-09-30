#ハングマンゲームの再現。答えの単語をリストからランダムに選ぶように設定する。
import random

words = ["python", "java", "javascript", "html", "css"]
word = random.choice(words)

def hangman(word):
    wrong = 0
    stages = ["",
              "________        ",
              "|       |       ",
              "|       O       ",
              "|      /|\      ",
              "|      / \      ",
              "|               "]
    
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("あなたの勝ち！正解は {}.".format(word))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong+1]))
'''
wrong+1にした理由は、wrongは間違えた回数をカウントしているため、 
ステージのリストのインデックスとして使用する際に、
正しいステージを表示するために1を加える必要があるからです。
例えば、wrongが0の場合、
最初のステージ（空の状態）を表示するためにstages[0:1]を使用します。
wrongが最大値を取った場合は、
最後のステージ（完全なハングマン）を表示するために
stages[0:wrong+1]を使用します。'''

print("あなたの負け！正解は {}.".format(word))
        
hangman(word)