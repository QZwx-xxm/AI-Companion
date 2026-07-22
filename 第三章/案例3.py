# 需求1：将1-1000之间（含1000）所有的5的倍数的数字累加起来
# sum = 0
# for i in range(1, 1001):
#    if i % 5==0:
#        sum+=i
# print(sum)


#需求2：统计字符串 "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd" 字符串中有多少个a和k
s = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
a_num = 0
k_num = 0
for i in s :
    if i == "a":
        a_num+=1
    if i == "k":
        k_num+=1
print(f"字符串中a的数量有：{a_num}，k的数量有：{k_num}")