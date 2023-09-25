#teoriya
# f = open("qwerty.txt")
# k = 0
# for x in f:
#     s = list(map(int, x.split())) //.split nado chtob stroky chisel prevratit' v spisok-massiv
#     s.sort() //sortiryet chisla v poryadke vozrastania
#     if <uslovie>:
#         k += 1
# print(k)


# PRACTICA >>>

# reshu ege №45243
# f = open("qwerty.txt")
# k = 0
# for x in f:
#     s = list(map(int, x.split()))
#     s.sort()
#     if (s[0] + s[4]) ** 2 > s[1]**2 + s[2]**2 + s[3]**2:
#         k += 1
# print(k)

#reshu ege №47213
# f = open("qwerty.txt")
# k = 0
# for x in f:
#     s = list(map(int, x.split()))
#     s.sort()
#     if len(set(s)) == 5: //set ydalyaet iz stroki povtor znacheniya
#         sum_povt = 0
#         sum_nepovt = 0
#         for i in s:
#             if s.count(i) == 2:
#                 sum_povt += i
#             else:
#                 sum_nepovt += i
#         if sum_nepovt / 4 <= sum_povt:
#             k += 1
# print(k)


#reshu ege №51978
# f = open("qwerty.txt")
# k = 0
# for x in f:
#     s = list(map(int, x.split()))
#     s.sort()
#     if len(set(s)) == 5:
#         sum_ch = 0
#         sum_nech = 0
#         cnt_ch = 0
#         cnt_nech = 0
#         for i in s:
#             if i % 2 == 0:
#                 cnt_ch += 1
#                 sum_ch += i
#             else:
#                 cnt_nech += 1
#                 sum_nech += i
#         if sum_nech < sum_ch and cnt_nech > cnt_ch:
#             k += 1
# print(k)


#https://clck.ru/35r3v2 - ssilka na test


# f = open("qwerty.txt")
# k = 0
# for x in f:
#     s = list(map(int, x.split()))
#     s.sort()
#     sum1 = 0
#     for i in s:
#         sum1 += i
#     if sum1 % 18 == 0:
#         k += 1
# print(k)


f = open("qwerty.txt")
k = 0
for x in f:
    s = list(map(int, x.split()))
    s.sort()
    sum_ch = 0
    sum_nech = 0
    srzn_ch = 0
    srzn_nech = 0
    cnt_ch = 0
    cnt_nech = 0
    for i in s:
        if i % 2 == 0:
            sum_ch += i
            cnt_ch += 1
        else:
            sum_nech += i
            cnt_nech += 1
    if cnt_ch == 0:
        srzn_ch = 0
    else:
        srzn_ch = sum_ch / cnt_ch
    if cnt_nech == 0:
        srzn_nech = 0
    else:
        srzn_nech = sum_nech / cnt_nech
    if abs(srzn_ch - srzn_nech) > 50 and not(len(set(s)) == 5) or not(abs(srzn_ch - srzn_nech) > 50) and len(set(s)) == 5:
        k += 1
print(k)


# f = open("qwerty.txt")
# k = 0
# for x in f:
#     s = list(map(int, x.split()))
#     s.sort()
#     sum_povt = 0
#     sum_nepovt = 0
#     srzn_povt = 0
#     srzn_nepovt = 0
#     if len(set(s)) == 5:
#         for i in s:
#             if s.count(i) == 2:
#                 sum_povt += i * 2
#             else:
#                 sum_nepovt += i
#         srzn_povt = sum_povt / 2
#         srzn_nepovt = sum_nepovt / 4
#         if srzn_nepovt >= srzn_povt:
#             k += 1
# print(k)
