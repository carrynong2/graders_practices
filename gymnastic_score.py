s1, s2, s3,s4 = input().split(" ")
s1 = float(s1)
s2 = float(s2)
s3 = float(s3)
s4 = float(s4)

min_s = s1
if s2 < min_s:
  min_s = s2
if s3 < min_s:
  min_s = s3
if s4 < min_s:
  min_s = s4

max_s = s1
if s2 > max_s:
  max_s = s2
if s3 > max_s:
  max_s = s3
if s4 > max_s:
  max_s = s4
s = (s1 + s2 + s3 + s4 - min_s - max_s) / 2
print(round(s,2))