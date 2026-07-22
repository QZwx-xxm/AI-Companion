# 需求描述
# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
# 1.添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2.修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 3.删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# 4.查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 5.列出所有学生：遍历所有学生信息并输出。
# 6.统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
# 7.退出系统
bet = """
#################################################【菜单】#################################################
# 1. 添加学生信息  2. 修改学生信息  3. 删除学生信息  4. 查询学生信息  5. 列出所有学生  6. 统计班级成绩  7. 退出系统 #
#########################################################################################################
"""
student_information = {}
while True:
    print(bet)
    choice = input("请输入您的选择：(1-7):")
    match choice:
        case "1":
            student_name = input("请输入需录入学生姓名:")
            if student_name in student_information:
                print("已存在此学生，请重新选择！")
            else:
                student_chinese = float(input("请输入此学生语文成绩:"))
                student_math = float(input("请输入此学生数学成绩:"))
                student_english = float(input("请输入此学生英语成绩:"))
                student_information[student_name] = {"chinese": student_chinese, "math": student_math,
                                                     "english": student_english}
                print("学生信息录入成功！！！")
        case "2":
            student_name = input("请输入需修改信息的学生姓名:")
            if student_name not in student_information:
                print("不存在此学生，请重新选择！")
            else:
                student_chinese = float(input("请输入学生需修改语文成绩:"))
                student_math = float(input("请输入学生需修改数学成绩:"))
                student_english = float(input("请输入学生需修改英语成绩:"))
                student_information[student_name] = {"chinese": student_chinese, "math": student_math,
                                                     "english": student_english}
                print("学生信息修改成功！！！")
        case "3":
            student_name = input("请输入需删除信息的学生姓名:")
            if student_name not in student_information:
                print("不存在此学生，请重新选择！")
            else:
                del student_information[student_name]
                print("学生信息删除成功！！！")
        case "4":
            student_name = input("请输入需查询信息的学生姓名:")
            if student_name not in student_information:
                print("不存在此学生，请重新选择！")
            else:
                info_name = student_information[student_name]
                print((f"学生姓名：{student_name}"
                       f"语文成绩：{info_name["chinese"]}"
                       f"数学成绩：{info_name["math"]}"
                       f"英语成绩：{info_name["english"]}"))
        case "5":
            for student_name in student_information:
                info_name = student_information[student_name]
                print((f"学生姓名：{student_name}，"
                       f"语文成绩：{info_name["chinese"]}，"
                       f"数学成绩：{info_name["math"]}，"
                       f"英语成绩：{info_name["english"]}"))
        case "6":
            chinese_score = []
            math_score = []
            english_score = []
            if not student_information:
                print("暂无学生数据，请先输入学生信息！！！")
            else:
                for student_name in student_information:
                    info_name = student_information[student_name]  # dict[key]=viules,key!=valuse
                    chinese_score.append(info_name["chinese"])
                    math_score.append(info_name["math"])
                    english_score.append(info_name["english"])
                print(
                    f"语文：最高分：{max(chinese_score)}，最低分：{min(chinese_score)}，平均分：{sum(chinese_score) / len(chinese_score):.1f}")
                print(
                    f"数学：最高分：{max(math_score)}，最低分：{min(math_score)}，平均分：{sum(math_score) / len(math_score):.1f}")
                print(
                    f"英语：最高分：{max(english_score)}，最低分：{min(english_score)}，平均分：{sum(english_score) / len(english_score):.1f}")
                for name, info in student_information.items():
                    if info["chinese"] == max(chinese_score):
                        print(f"语文最高分：{max(chinese_score)}的学生名字是{name}")
                    if info["chinese"] == min(chinese_score):
                        print(f"语文最低分：{min(chinese_score)}的学生名字是{name}")
                    if info["math"] == max(math_score):
                        print(f"数学最高分：{max(math_score)}的学生名字是{name}")
                    if info["math"] == min(math_score):
                        print(f"数学最低分：{min(math_score)}的学生名字是{name}")
                    if info["english"] == max(english_score):
                        print(f"英语最高分：{max(english_score)}的学生名字是{name}")
                    if info["english"] == min(english_score):
                        print(f"英语最低分：{min(english_score)}的学生名字是{name}")
        case "7":
            break
        case _:
            print("非法输入，请重试！！！")
