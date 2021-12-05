from randomgen import Xoroshiro128
f_r = str(Xoroshiro128().state['s'][0])
if int(f_r[-1]) <= 3:
    mint_p = int(f_r[-2] + f_r[-3] + f_r[-4])
elif int(f_r[-1]) == 9:
    mint_p = int(f_r[-2] + f_r[-3] + f_r[-4] + f_r[-5] + f_r[-6])
else:
    mint_p = int(f_r[-2] + f_r[-3] + f_r[-4] + f_r[-5])
print(mint_p)
