import jellyfish


def lv_sim(lv_dist, l_max):
    return 1.0 - lv_dist/l_max
def hm_sim(hm_dist, l_max):
    return 1.0 - hm_dist/l_max

f = open("test.txt", "r", -1, 'UTF-8')
lines = f.readlines()
for i in lines:
    print(i)

test_str = u'포스텍에 김진모라는 사람 있어?\n'

for i in lines:
    print(i)
    print('JARO-WINKLER')
    print(jellyfish.jaro_winkler(test_str, i))
    print('LEVENSHTEIN')
    lv_sim = 1.0 - jellyfish.levenshtein_distance(test_str, i) / max(len(test_str), len(i))
    print(lv_sim)
    print('HAMMING')
    hm_sim = 1.0 - jellyfish.hamming_distance(test_str, i) / max(len(test_str), len(i))
    print(hm_sim)
    print('\n')

real_test_str = u'포스텍에 한주완 있어?'
sim = 0
for i in lines:
    sim = lv_sim(jellyfish.levenshtein_distance())
'''
lv_dist = 1000000000
lv_str = ''
jw_dist = 0

for i in lines:
    if lv_dist > jellyfish.levenshtein_distance(test_str, i):
        lv_dist = jellyfish.levenshtein_distance(test_str, i)
        print(lv_dist)
        lv_str = i
print(lv_str)
'''