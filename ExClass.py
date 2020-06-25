class Student:
    
    def __init__(self,name,k,e,m):
        self.name=name
        self.kor = k;
        self.eng = e;
        self.mat = m;
        self.total = k+e+m;
        self.avg = self.total/3.0

    def __init__(self ):
        self.name=None
        self.kor = 0;
        self.eng = 0;
        self.mat = 0;
        self.total = 0;
        self.avg = 0

    def setName(self,name):
        self.name = name

    def setKor(self,kor):
        self.kor = kor
    def setEng(self,eng):
        self.eng = eng
    def setMat(self,mat):
        self.mat = mat

    def setTotal(self):
        self.total = self.kor+self.eng+self.mat

    def setAvg(self):
        self.setTotal()
        self.avg = self.getTotal()/3.0
    
    def getName(self):   
        return self.name

    def getKor(self):
        return self.kor
    def getEng(self):
        return self.eng
    def getMat(self):
        return self.mat

    def getTotal(self):
        self.setTotal()
        return self.total
    def getAvg(self):
        self.setAvg()
        return self.avg

    
#james = Student('Superman',10,20,30)  # init메소드 호출
james = Student()

james.setName('superman')
james.setKor(10)
james.setEng(20)
james.setMat(30)

print(james.getName(),end=' ')
print(james.getKor(),end=' ')
print(james.getEng(),end=' ')
print(james.getMat(),end=' ')
print(james.getTotal(),end=' ')
print(james.getAvg())
