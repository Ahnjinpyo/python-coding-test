korean = int(input())
math = int(input())
english = int(input())

if korean < 0 or korean > 100 or math < 0 or math > 100 or english < 0 or english > 100:
    print("invalid socre")

avg = (korean + math + english) / 3

if avg >= 80 or avg <= 100:
    print("fail")
else:
    print("success") 