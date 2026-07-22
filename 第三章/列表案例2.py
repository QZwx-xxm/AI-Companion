# 合并两个列表中的元素，并对合并的结果进行去重处理（去除列表中的重复元素）。
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
num_list3 = num_list1+num_list2
num_list4=[]
print(num_list3)
for i in num_list3:
    print(i)
    if i not in num_list4:
        num_list4.append(i)
print("去重后的列表为：",num_list4)