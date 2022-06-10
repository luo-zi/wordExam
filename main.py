import random
import threading

import pyttsx3 as pt


def main(name):
    """
    name: 没啥用,懒得删
    info:
    读入词汇表文件到列表
    使用随机索引取出列表项
    打印中文意思, 等待用户输入英文
    给出正误反馈
    退出后结算练习次数和成功率

    ===============================
    词汇表的格式要求(一行):
    ------------------
    英文 中文
    ------------------
    英文与中文间隔一个空格, 不得出现前导空格与尾部空格
    """
    wordsList = []
    success = 0
    failure = 0

    with open("./out1.txt", "r", encoding="UTF-8") as f:  # out.txt是EnglishLevelTwo.txt经过几个函数的处理后, 格式良好的词汇表文件
        l = f.readlines()
        for x in l:
            kv = x.split(" ")
            wordsList.append((kv[0], kv[1]))

    print("根据中文意思写出英文单词")
    print("输入 '=' 以退出")

    r = random.randint
    while True:
        listItem = wordsList[r(0, len(wordsList) - 1)]

        sound = threading.Thread(target=(lambda x: pt.speak(x)), args=(listItem[0],))
        sound.start()
        inputStr = input(listItem[1] + "提示:" + (listItem[0])[0:3] + "\n")
        if inputStr == "=":
            break
        elif inputStr == listItem[0]:
            print("+ Yeeeees~~~")
            success += 1
        else:
            print("- Noooooooo")
            failure += 1
            print(f"Is {listItem[0]}")

    successRate = 0 if success == 0 else round(success / (success + failure) * 100, 1)

    print(f"共练习:{success + failure}次,成功率:{successRate}%")


#
# def FormatTheText(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     outText = ""
#     with open("./out1.txt","r") as f:
#         fList=f.readlines()
#         outList=list(map(StripSpace,fList))
#         for x in outList:
#             outText+=x
#     with open("./out1.txt","x") as f:
#         f.write(outText)
#         f.flush()
#
# def StripSpace(s:str):
#     r=""
#     space=False
#     for x in s:
#         if space and x ==" ": #如果已经遇到空格,则跳过
#             continue
#         if x==" ":
#             space=True
#         r+=x
#     return  r

if __name__ == '__main__':
    main('PyCharm')
