#(C)Tsubasa Kato 4/14/2022
import arrayfire as af
af.set_backend('cuda') 
x = 0
while (x <= 100):
  print(af.cbrt(af.randu(2,2)))
  x = x + 1