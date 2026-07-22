# 1.定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积 = 底 * 高 / 2）。
# 2.定义一个函数：计算传入的字符串中元音字母的个数（元音字母为 aeiouAEIOU）。
# 3.定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留1位小数），并返回。
def triangle_area(height,base):
    """
    根据传入的底和高计算三角形面积的函数
    :param height:代表三角形的高度
    :param base: 代表三角形的底长
    :return area: 三角形的面积
    """
    area = (base * height)/2
    return area

def number_letters (s):
    """
    计算传入的字符串中元音字母的个数
    :param s: 代表字符串
    :return count: 代表字符串中元音字母的个数
    """
    count=0
    vowel = ('a','e','i','o','u','A','E','I','O','U')
    for i in s:
        if i in vowel:
            count+=1
    return count

def class_score(list1):
    """
    计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分
    :param list1: 班级学员高考成绩列表
    :return max_score,min_score,avg_score: 成绩的最高分、最低分、平均分
    """
    max_score=max(list1)
    min_score=min(list1)
    avg_score=round(sum(list1)/len(list1),1)
    return max_score,min_score,avg_score