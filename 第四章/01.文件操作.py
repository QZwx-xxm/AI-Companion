# # 读文件
# # 1.打开文件
# f = open("resources/望庐山瀑布.txt", "r", encoding="utf-8")
#
# # 2.读取文件
# # content=f.read()
# # print(content)
#
# content_list = f.readlines()
# for line in content_list:
#     print(line.strip())
#
# # 3.关闭文件
# f.close()

# 写文件
# 1.打开文件
# word=open("resources/静夜思.txt", "w", encoding="utf-8")
#
# # 2.写入文件内容
# word.write("静夜思\n")
# word.write("\n")
# word.write("窗前明月光，\n")
# word.write("疑是地上霜，\n")
# word.write("举头望明月，\n")
# word.write("低头思故乡。\n")
#
#
# # 3.关闭文件
# word.close()

with open("resources/静夜思.txt", "w", encoding="utf-8") as word:

# 2.写入文件内容
    word.write("静夜思\n")
    word.write("\n")
    word.write("窗前明月光，\n")
    # i = 1 / 0
    word.write("疑是地上霜，\n")
    word.write("举头望明月，\n")
    word.write("低头思故乡。\n")
