# Ввод ответа тестирующей системы и ответа школьника
test_answer = int(input())
student_answer = int(input())

# Проверка корректности ответа школьника
if test_answer == 1:
    if student_answer == 1:
        print("YES")
    else:
        print("NO")
else:
    if student_answer == 1:
        print("NO")
    else:
        print("YES")