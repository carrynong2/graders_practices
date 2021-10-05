code = input()
faccodes = ["01","02","51","53","55","58"]
if len(code) == 2 and  "0" <= code[1] <= "9"  and "20" <= code <= "40" or code in faccodes:
  print("OK")
else:
  print("Error")