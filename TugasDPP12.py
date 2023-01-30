from BULLET_TRAIN import sinopis as Sinop
from cek_huruf import cek_huruf
from cek_kapital import cek_jumlah_kapital
from cek_kata import cek_kata

print(Sinop,end='\n')

line=''
for i in range (50):
    line+='-'
print(line)
    

cek_kata(Sinop)
cek_huruf(Sinop)
cek_jumlah_kapital(Sinop)





