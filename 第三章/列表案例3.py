# 1.生成1-20的平方列表。
# 2.从如下数字列表中提取所有偶数，并计算其平方，组成一个新的列表。
# num_list=[19,23,54,64,87,20,109,232,123,43,26,55,72]

# ping_list=[]
# num = 0
# for i in range(1,21):
#     num=i**2
#     ping_list.append(num)
# print(ping_list)

num_list=[19,23,54,64,87,20,109,232,123,43,26,55,72]
num=0
number_list =[]
for i in num_list:
    if i %2==0:
        num = i **2
        number_list.append(num)
print(number_list)