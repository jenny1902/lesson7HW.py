stu = (int(input("請輸入學生的數量: ")))
score = []
high = 0
low = 100
for i in range(stu):
    c = (int(input("請輸入學生的數學成績: ")))
    name = input("請輸入學生的成績: ")
    score.append(c)
high = max(score)
low = min(score)
summ = sum(score)
avg = summ/stu
print("全班總分:", summ, "分")
print("全班平均:",avg,"分")
print("全班最高分:",high,"分")
print("全班最低分:",low,"分")