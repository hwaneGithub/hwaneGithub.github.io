# 1. Student Class -------------------------------------------------------------------------

class Student:
     def __init__(self, name, kor, eng, math):
          self.name = name
          self.kor = kor
          self.eng = eng
          self.math = math
          self.total = (kor + eng + math)
          self.avg = self.total / 3


          
# 2. StudentList Class ---------------------------------------------------------------------

class StudentList:
     def __init__(self):
          self.student_list = []

     def append_student(self, student):
          self.student_list.append(student)
          return self.student_list



# 3. ManageStudent Class -------------------------------------------------------------------

class ManageStudent(Student):
     def __init__(self):
          super().__init__()

     
## 1) 성적 입력
          
     @staticmethod
     def info_input():
          print('===========================================================================================')
          print('\n<< 1. 학생 정보 입력 >>')
          print()
          name = input('학생 이름: ')
     
          for person in student:
               if (person[0] == name):
                    print('이미 존재하는 학생입니다.')
                    return
               
          kor = int(input('국어 점수: '))
          if (kor < 0 and kor > 100):
               print('유효하지 않은 값입니다.')
               
          eng = int(input('영어 점수: '))
          if (eng < 0 and eng > 100):
               print('유효하지 않은 값입니다.')
               
          math = int(input('수학 점수: '))
          if (math < 0 and math > 100):
               print('유효하지 않은 값입니다.')

          total = (kor + eng + math)
          avg = total / 3
          student.append([name, kor, eng, math, total, avg])

          print()
          print('점수가 입력되었습니다.\n')
          print('===========================================================================================')


## 2) 성적 출력
          
     @staticmethod
     def info_out():
         print('===========================================================================================\n')
         for idx, person in enumerate(student):
             print('-----------------')
             print('이름: ', person[0])
             print('국어: %3d' % person[1])
             print('영어: %3d' % person[2])
             print('수학: %3d' % person[3])
             print('-----------------')
             print('총점: %3d' % person[4])
             print('평균: %2f' % person[5])
             print('-----------------')
         print('\n===========================================================================================')


## 3) 정보 검색

     @staticmethod
     def info_search():
          print('===========================================================================================\n')
          print(' 검색 기준을 선택하세요.(1.이름 2.기준 평균 점수): \n')
          choice = int(input())
          print('\n===========================================================================================')
          if choice == 1:
              name = input('\n검색을 원하는 이름을 입력하세요: ')
              for person in student:
                  if person[0] == name:
                      print('-----------------')
                      print('이름: ', person[0])
                      print('국어: %3d' % person[1])
                      print('영어: %3d' % person[2])
                      print('수학: %3d' % person[3])
                      print('-----------------')
                      print('총점: %3d' % person[4])
                      print('평균: %2f' % person[5])
                      print('\n===========================================================================================')
                      return
                    
                  else:
                      print('\n!!해당 정보가 목록에 존재하지 않습니다!!')
                      
          elif choice == 2:
              standard = float(input('기준 평균 점수를 입력하세요:\n '))
              for person in student:
                  if person[5] >= standard:
                      print('-----------------')
                      print('이름: ', person[0])
                      print('국어: %3d' % person[1])
                      print('영어: %3d' % person[2])
                      print('수학: %3d' % person[3])
                      print('-----------------')
                      print('총점: %3d' % person[4])
                      print('평균: %2f' % person[5])
                      print('\n===========================================================================================')

          else:
              print('잘못 입력되었습니다. 다시 선택하세요.')

                          
## 4) 정보 삭제

     @staticmethod
     def info_delete():
          print('---------------------------------------------')
          name = input('삭제를  원하는 이름을 입력하세요: ')

          for idx, person in enumerate(student):
               if (person[0] == name):
                    del student[idx]
                    return
          print('\n!!해당 정보가 목록에 존재하지 않습니다!!')          


## 5) 정보 수정
          
     @staticmethod
     def info_modify():
          print('---------------------------------------------')
          name = input('수정을 원하는 이름을 입력하세요: ')

          for person in student:
               if (person[0] == name):
                    kor = int(input('국어: '))
                    if (0 <= kor <= 100):
                         person[1] = kor
                    else:
                         print('유효하지 않은 값입니다.')

                    eng = int(input('영어: '))
                    if (0 <= eng <= 100):
                         person[2] = eng
                    else:
                         print('유효하지 않은 값입니다.')

                    math = int(input('수학: '))
                    if (0 <= math <= 100):
                         person[3] = math
                    else:
                         print('유효하지 않은 값입니다.')

                    person[4] = person[1] + person[2] + person[3]
                    person[5] = person[4] / 3
                    return

               else:
                    print('해당 정보가 목록에 존재하지 않습니다.')
          print('\n수정 완료되었습니다.')
                    
## 6) 파일 관리

     @staticmethod
     def info_file():
          import pickle

          print('---------------------------------------------')
          print('1. 저장하기 2. 불러오기')
          num = int(input('원하는 작업의 번호를 입력하세요: '))
          if (num == 1):
               with open('Student_Info.txt', 'wb') as file:
                    pickle.dump(student, file)
                    print('======================')
                    print('@저장이 완료되었습니다.')

          elif (num == 2) :
               with open('Student_Info.txt', 'rb') as file:
                    s = pickle.load(file)
                    print(s)
                    print('======================')
                    print('@저장된 정보를 불러오겠습니다.')

          else:
               print('유효하지 않은 값입니다.')



# 4. Main ----------------------------------------------------------------------------------

student = []

while True:
     print('\n<< 학생 성적 관리 프로그램 >>')
     print('===========================================================================================')
     print(' 1. 점수 입력\t 2. 정보 출력\t 3. 정보 검색\t 4. 정보 삭제\t 5. 정보 수정\t 6. 파일화')
     print('===========================================================================================')
     menu = int(input('\n메뉴를 선택하세요: '))
     print()

     if menu == 1:
          ManageStudent.info_input()
     elif menu == 2:
          ManageStudent.info_out()
     elif menu == 3:
          ManageStudent.info_search()          
     elif menu == 4:
          ManageStudent.info_delete()
     elif menu == 5:
          ManageStudent.info_modify()
     elif menu == 6:
          ManageStudent.info_file()
                    
     else:
          print('\n<프로그램을 종료합니다.>')
          break

          
