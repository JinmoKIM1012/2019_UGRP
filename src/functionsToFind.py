from konlpy.tag import Okt
from konlpy.tag import Hannanum


Proper_Noun = ['포스텍', '포항공대', '학교', '우리학교', '우리', '사람', '이메', '이메일', '학번', '학', '과',
               '번', '라', '몇', '무슨', '어느', '어떤', '좀', '뭐', '도로명', '텍', '명', '기계공']


def get_noun(input_text):
    okt = Okt()
    hannanum = Hannanum()

    nouns = okt.nouns(input_text)
    hannanum_nouns = hannanum.nouns(input_text)

    nouns = nouns + hannanum_nouns
    # 모든 noun이 nouns에 들어있다.

    for i in Proper_Noun:
        for j in nouns:
            if i == j:
                nouns.remove(i)
    return nouns


def get_name_only(input_nouns):
    try:
        new_nouns = []

        # 길이 1 또는 4이상 요소 삭제
        for i in input_nouns:
            now_length = len(i)
            if not (now_length == 1 or now_length >= 4):
                new_nouns.append(i)

        # 이름 결정
        found_name = new_nouns[0]

        for i in new_nouns:
            if len(i) > len(found_name):
                found_name = i
        return found_name
    except:
        return None


def get_department(nouns):
    department = []
    no_department = []
    new_nouns = []

    # 길이 1 요소 삭제
    for i in nouns:
        now_length = len(i)
        if not now_length == 1:
            new_nouns.append(i)

    # 배열 분리용
    for i in new_nouns:
        if i[::-1][0] == '과' or i == '무은재학부':
            department.append(i)
        else:
            no_department.append(i)

    # 학과 결정
    if len(department) == 0:
        return 'no_department', no_department

    department_name = department[0]

    for i in department:
        if len(i) > len(department_name):
            department_name = i

    # 학과 이름, 학과 이름이 빠진 배열 반환
    return department_name, no_department


if __name__ == '__main__':
    test_text = '기계공학과에 조은찬 있어?'
    noun_lst = get_noun(test_text)
    dpt, new_noun = get_department(noun_lst)
    name = get_name_only(new_noun)
    print(dpt, name)