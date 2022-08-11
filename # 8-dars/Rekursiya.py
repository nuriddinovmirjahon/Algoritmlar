# REKURSIYA bu  - bir narsa ichidagi narsani yana takrorlanishi
# masalan: bizda 4 ta karobka bor. ulani bittasini ichida bizga kereli kalit bo . 
# biz u kalitti toishimiz kere 1 karobkani ochamiz agar uni ichida kalit bo'sa 
# o'sha zahoti qidirishni to'xtashi kere agar kalit bo'masa keyingi karobkani ochish kere
# 1 karobka bo'sh bo'sa ikkinchisini ochib ko'radi shu REKURSIYA deyiladi.
#
#       REKURSIYA funksiyalar 2 qismdan iborat bo'ladi
#           Rekursiya sharti (recursive carse)
#           To'xtash sharti (bace case)
#
#
#
#
#
#
#
#
#


def sana(n):
    print(n)
    if n<=1:
        return
    else:
        sana(n-1)

sana(10)