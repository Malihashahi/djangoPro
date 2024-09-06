
def finder5(adad):
  adad_str = str(adad)
  tedad =0
  for x in range(len(adad_str)):
    if adad_str[x] == "5":
      tedad=tedad+1

  return tedad     

taded_kol =0

for i in range(1,1001):
   taded_kol =taded_kol+ finder5(i)

print(taded_kol)
