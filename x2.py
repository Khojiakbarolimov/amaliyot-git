n = int(input("Elementlar soni: "))
lst = []
for i in range(0, n):
    lst.append(int(input("Enter the number: ")))
max = 0
for i in range(1, len(lst)):
    temp = abs(lst[i-1] - lst[i])
    if temp > max:
        max = temp
        values = [lst[i-1], lst[i]]
print(f"{max}({values[0]} va {values[1]})")