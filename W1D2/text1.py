# 班级成绩数据
students = [
    {"学号": "001", "姓名": "张三", "班级": "1班", "高数": 85, "英语": 78, "Java编程": 92},
    {"学号": "002", "姓名": "李四", "班级": "1班", "高数": 90, "英语": 88, "Java编程": 76},
    {"学号": "003", "姓名": "王五", "班级": "2班", "高数": 55, "英语": 60, "Java编程": 45},
    {"学号": "004", "姓名": "赵六", "班级": "2班", "高数": 95, "英语": 70, "Java编程": 85},
    {"学号": "005", "姓名": "孙七", "班级": "1班", "高数": 60, "英语": 55, "Java编程": 50},
]

# 科目列表（排除非成绩字段）
subjects = ["高数", "英语", "Java编程"]

# ---------- 1. 计算每个学生的总分 ----------
for stu in students:
    stu["总分"] = sum(stu[sub] for sub in subjects)

# ---------- 2. 求单科第一 ----------
def find_top(subject):
    max_score = max(stu[subject] for stu in students)
    top_students = [stu["姓名"] for stu in students if stu[subject] == max_score]
    return top_students, max_score

print("========== 单科第一 ==========")
for sub in subjects:
    names, score = find_top(sub)
    print(f"{sub}：{score} 分，学生：{', '.join(names)}")

# ---------- 3. 求总分第一 ----------
max_total = max(stu["总分"] for stu in students)
top_total = [stu["姓名"] for stu in students if stu["总分"] == max_total]
print(f"\n总分第一：{max_total} 分，学生：{', '.join(top_total)}")

# ---------- 4. 挂科名单（任意一门 < 60 即算挂科） ----------
failed = [stu["姓名"] for stu in students if any(stu[sub] < 60 for sub in subjects)]
print(f"\n挂科学生名单：{', '.join(failed) if failed else '无'}")

# 显示详细挂科情况
print("\n========== 挂科详情 ==========")
for stu in students:
    failed_subs = [sub for sub in subjects if stu[sub] < 60]
    if failed_subs:
        print(f"{stu['姓名']} 挂科科目：{', '.join(failed_subs)}")