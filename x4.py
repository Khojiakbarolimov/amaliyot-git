month = {
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December"
}
def removezero(s: str)->str:
    if s[0].startswith("0"):
        s[0] = s[0].removeprefix("0")
    if s[1].startswith("0"):
        s[1] = s[1].removeprefix("0")
    return s
date = input("Enter the date(mm.dd.yy): ").split(".")
time = input("Enter the time(hh:mm): ").split(":")

date, time = removezero(date), removezero(time)

print(f"{date[1]} {month[int(date[0])]} {date[2]} year")
print(f"{time[0]} hours {time[1]} minutes")