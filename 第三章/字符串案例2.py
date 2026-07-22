# 1.输入一个字符串，判断该字符串是否是回文（两边对称）。
#
# - 黄山落叶松叶落山黄
# - 上海自来水来自海上
#
# 2.将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来。


# word = input("请输入一段文字（诗歌）：")
# if word == word[::-1]:
#     print(f"{word}是回文")
# else:
#     print(f"{word}不是回文")

# still_str=[]
# for i in range(0,10):
#     word = input("请输入的一个字符串：")
#     new_word = word[::-1]
#     still_str.append(new_word.upper())
# print(still_str)

lst = []
new_text=[]
for i in range(10):
    text = input(f"请输入第{i+1}个字符串：")
    new_text.append(text)
new_text.reverse()
for i in new_text:
    lst.append(i.upper())
for item in lst:
    print(item)