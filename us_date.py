d,m,y = input().split("/")
m = int(m)
months = [
  "January","February","March","April","May","June","July","August","September","October","November","December"
]
print(months[m - 1], d + ",", y)