n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
records = 0
for k, v in student_marks.items():
    if k == query_name: records = v
ave = 0
for s in records:
    ave = ave+s
print("%.2f" % (ave/3))