# 성적 처리 프로그램

# stu : 이름(키) : 국(kor), 영(eng), 수(math), 총점(tosc), 평균(avg)

# 기능
'''
------------------------------------------------------------------
- 딕셔너리 생성
- 메뉴선택(1~6번 중 하나 선택)


1. 입력(ip) : 이름, 국, 영, 수
- 각 값 입력 : input()
- 입력값 딕셔너리에 저장
- 저장 알림 텍스트
- 메뉴로 나가기


2. 출력(op) : 전체 출력
- 딕셔너리에 입력된 값 출력 = print(stu)
- 메뉴로 나가기


3. 검색(sear) : 이름 검색 후 한 사람 정보 출력, 평균 입력 시 입력 평균 이상의 정보 출력
- 이름 검색창
- 검색된 해당 딕셔너리 불러오기 : 딕셔너리변수.get('키')
- 해당 딕셔너리의 평균 이상인 딕셔너리 출력

                   
4. 삭제(rem) : 이름 검색 삭제
- 딕셔너리변수.pop('키')

5. 수정(edit) : 국, 영, 수, 중 수정 시 총점, 평균 다시 계산 처리
- 딕셔너리변수.update(키=수정할 값)

6. 파일처리(지속적으로 데이터 사용)(mag)
-


모듈화 사용
'''     
#--------------------------------------------------------------------------------------------------------

def insert(stu):
    name = input('학생 이름 입력 : ')

    if (name not in stu):
        kor = int(input('국어 점수 : '))                    
        eng = int(input('영어 점수 : '))
        math = int(input('수학 점수 : '))
        score = kor+eng+math
        avg = round(score/3, 2)
        print('성적이 입력되었습니다.')
        print()

    else:
        print('이미 있는 학생입니다. 다시 입력해주세요.')
        print()
        return insert(stu)

    stu[name] = [kor, eng, math, score, avg]
    person = stu[name]
    return stu

#--------------------------------------------------------------------------------------------------------
    
def view(stu):

    print('| 이름 | 국 | 영 | 수 | 총점 | 평균 |')
    
    for key, value in stu.items():
        print(key,':', value)
    
    print()        
    return stu

# '목록이 없습니다' 추가

#--------------------------------------------------------------------------------------------------------

def search(stu):
    name = input('검색할 학생 이름 : ')

    if (name in stu):
        print('| 이름 | 국 | 영 | 수 | 총점 | 평균 |')
        print(name, stu.get(name))
        print()

    else:
        print('존재하지 않는 학생입니다. 이름을 다시 확인해주세요.')
        print()
        
    return stu

#--------------------------------------------------------------------------------------------------------
    
def edit(stu):
    name = input('수정할 학생 이름 : ')

    if (name in stu):
        print('국어, 영어, 수학 성적을 입력해주세요.(,로 구분) : ')
        kor, eng, math = map(int, input().split(','))
        score = kor+eng+math
        avg = round(score/3, 2)
        print()

    else:
        print('존재하지 않는 학생입니다. 이름을 다시 확인해주세요.')
        print()

    stu[name] = [kor, eng, math, score, avg]
    person = stu[name]
    return stu

#--------------------------------------------------------------------------------------------------------

def delete(stu):
    name = input('삭제할 학생 이름 : ')

    if (name in stu):
        stu.pop(name)
        print('삭제되었습니다.')
        print()

    else:
        print('존재하지 않는 학생입니다. 이름을 다시 확인해주세요.')
        print()

    return stu

#--------------------------------------------------------------------------------------------------------
'''
def makeFile(stu):

    import pickle

    with open("student's_score.txt", 'wb') as file:
        pickle.dump(stu, file)

'''
'''
    file = open("student's_score.txt", 'w')
    file.write(stu)
    file.close()
'''
'''
    print('txt파일로 저장되었습니다.')
    print()

    return stu
'''
#--------------------------------------------------------------------------------------------------------

def main():
    stu = {}
    while True:
        print('성적 관리 프로그램입니다. 메뉴를 선택해주세요.')
        menu = int(input('| 1. 입력 | 2. 출력 | 3. 검색 | 4. 수정 | 5. 삭제 | 6. 파일처리 |\n'))

        if menu == 1 :
            stu = insert(stu)
        elif menu ==2:
            stu = view(stu)
        elif menu == 3:
            stu = search(stu)
        elif menu == 4:
            stu = edit(stu)
        elif menu == 5:
            stu = delete(stu)
        elif menu == 6:
            stu = makeFile(stu)
        else:
            print('종료되었습니다.')
            break

main()







'''
stu = {}

while True:
    print('| 1. 입력 | 2. 출력 | 3. 검색 | 4. 삭제 | 5. 수정 | 6. 파일처리 |')
    menu = int(input('메뉴를 선택하시오 : '))
             
    if menu == 1:
        while True:
            name = input('학생 이름 입력 : ')
            kor = int(input('국어 점수 : '))                    
            eng = int(input('영어 점수 : '))
            math = int(input('수학 점수 : '))
            score = kor+eng+math
            avg = round(score/3, 2)
            info = {'국어' : kor, '영어' : eng, '수학' : math, '총점' : score, '평균' : avg}
            stu.setdefault(name, info)
            print('성적이 입력되었습니다.')
            break
# 점수 범위 0~100 사이로
# 학생 이름 중복 문제 해결

                          
    elif menu == 2:
        while True:
            print(stu)
            break
# 2차원 배열 형태로 시각화

        
    elif menu == 3:
        while True:
            name = input('검색할 학생 이름 : ')
            print(stu.get(name))
            break
# 없는 이름 입력 시 검색결과가 없음, 메뉴 귀환 여부 출력

        
    elif menu == 4:
        while True:
            name = input('삭제할 학생 이름 : ')
            stu.pop(name)
            print('삭제되었습니다.')
            print('실행 결과')
            print(stu)
            break
            
            
    elif menu == 5:
        while True:
            name = input('수정할 학생 이름 : ')
            edit = input('수정할 과목 : ')
            if edit == '국어':
                stu.update(name=info.update('국어'=kor)
            elif edit == '영어':
                stu.update(name=info.update('영어'=eng)
            elif edit == '수학':
                stu.update(name=info.update('수학'=math)               
            else:
                print('잘못 누르셨습니다. 다시 입력해주십시오.')
            break

    
    elif menu == 6:
        while True:
        
    else:
        print('종료합니다.')
    exit()
'''
