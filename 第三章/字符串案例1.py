# 1.邮箱格式验证：用户输入一个邮箱，验证邮箱格式是否正确（包含一个@和至少一个.），如果输入正确，输出"邮箱格式正确"，否则输出"邮箱格式错误"。
# emli = input("请输入您的邮箱地址：")
# sum = 0
# for i in emli:
#     if i == "@":
#         for i in emli:
#             if i == ".":
#                 print("邮箱格式正确")
#                 sum = 1
# if sum == 0:
#     print("邮箱格式错误")

emli = input("请输入您的邮箱地址：")
if emli.count("@")==1 and emli.count(".")>=1:
    print("邮箱格式正确")
else:print("邮箱格式错误")
