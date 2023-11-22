def nama_fungsi():
  print("Hello World!")
nama_fungsi()

def hasil(nilai):
  if nilai < 60:
    return "Gagal"
  elif 61 <= nilai <= 70:
    return "Baik"
  elif 71 <= nilai <= 80:
    return "Sangat Baik"
  elif 81 <= nilai <= 100:
    return "Istimewa"
  else:
    return "nilai tidak ada"
print(hasil(100))

print()
def bilangan_ganjil(angka):
  for n in range(1, angka+1, 2):
    print(n, end=" ")
bilangan_ganjil(100) 
    
