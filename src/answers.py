import functionsToFind
from mysql_ReadStudentList import mysqlStudent


def find_10001(input_name):
    student_data = mysqlStudent()
    if student_data is None:
        return None
    else:
        name_list = [i[0] for i in student_data]
        return name_list.count(input_name)


def ANS_10001(name):  # name: 이름, string
    find = find_10001(name)  # find_0010001 은 함수로 입력된 name에 맞는 인원의 수(int)를 반환한다.

    if find == 0:  # 사람이 존재하지 않는 경우
        result = '포스텍에 ' + name + '이라는 사람이 존재하지 않습니다. 확인 후 다시 질문해 주세요.'
    elif find is None:
        result = 'DB 오류입니다. 다시 시도해주세요.'
    else:
        result = '예, 총 ' + str(find) + ' 명 검색 됩니다.'

    return result


'''
* 답변: 0010002, 이름으로 학번 검색
* 입력: ("이름")
'''


def find_10002(input_name):
    student_data = mysqlStudent()
    if student_data is None:
        return None
    else:
        return_list = []
        for student_name, student_num, student_dpt, student_email in student_data:
            if input_name == student_name:
                return_list.append(student_num)
        if len(return_list) == 0:
            return 1
        else:
            return return_list


def ANS_10002(name):  # name: 이름, string
    find = find_10002(name)

    if find is None:
        result = 'DB 오류입니다. 확인 후 다시 시도해주세요.'
    elif find == 1:
        result = '존재하지 않는 이름입니다. 확인 후 다시 말해주세요.'
    else:
        result = name + '님의 학번은 '
        for num in find:
            result += num + ' '
        result += '입니다.'
    return result


'''
* 답변: 0010003, 이름으로 학과 검색
* 입력: ("이름")
'''


def find_10003(input_name):
    student_data = mysqlStudent()
    if student_data is None:
        return None
    else:
        return_list = []
        for student_name, student_num, student_dpt, student_email in student_data:
            if input_name == student_name:
                return_list.append(student_dpt)
        if len(return_list) == 0:
            return 1
        else:
            return return_list


def ANS_10003(name):  # name: 이름, string
    find = find_10003(name)

    if find is None:
        result = 'DB 오류입니다. 확인 후 다시 시도해주세요.'
    elif find == 1:
        result = '존재하지 않는 이름입니다. 확인 후 다시 말해주세요.'
    else:
        result = name + '님의 학과는 '
        for dpt in find:
            result += dpt + ' '
        result += '입니다.'
    return result


'''
* 답변: 0010004, 이름으로 이메일 검색
* 입력: ("이름")
'''


def find_10004(input_name):
    student_data = mysqlStudent()
    if student_data is None:
        return None
    else:
        return_list = []
        for student_name, student_num, student_dpt, student_email in student_data:
            if input_name == student_name:
                return_list.append(student_email)
        if len(return_list) == 0:
            return 1
        else:
            return return_list


def ANS_10004(name):  # name: 이름, string
    find = find_10004(name)  # find_0010004 은 함수로 입력된 name에 맞는 이메일(string) 반환한다. (만약 존재하지 않는 경우 NULL을 반환한다.)

    if find is None:
        result = 'DB 오류입니다. 확인 후 다시 시도해주세요.'
    elif find == 1:
        result = '존재하지 않는 이름입니다. 확인 후 다시 말해주세요.'
    else:
        result = name + '님의 이메일은 '
        for email in find:
            result += email + ' '
        result += '입니다.'
    return result


'''
* 답변: 0010005, 이름으로 학과 소속 여부 검색
* 입력: ("이름"),("학과 이름")
'''


def ANS_10005(name, department):  # name: 이름, string
    find = find_10003(name)   # find_0010003 은 함수로 입력된 name에 맞는 학과이름(string) 반환한다. (만약 존재하지 않는 경우 NULL을 반환한다.)
    result = ''
    if find is None:
        result = 'DB 오류입니다. 확인 후 다시 시도해 주세요.'
    else:   # 사람이 존재하는 경우
        if find == 1:
            result = '해당하는 사람이 존재하지 않습니다.'
        else:
            for dpt in find:
                if department == dpt:  # 학과가 같은 경우
                    result = '네, 있습니다!'
                else:
                    result = '해당하는 이름이 학과에 존재하지 않습니다.'
    return result


'''
* 답변: 0020001, 학교 주소 검색
* 입력: ("이름")
'''


def ANS_20001():  # name: 이름, string
    result = '포스텍의 도로명 주소는 경상북도 포항시 남구 효곡동 청암로 77 입니다'
    return result


if __name__ == '__main__':
    txt = ANS_10005('좋은 찬', '무은재학부')
    print(txt)