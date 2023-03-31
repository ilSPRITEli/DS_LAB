class ProbHash:
    def __init__(self, cap):
        self.hashtable = cap * [None]
        self.n = cap
    def hashFunction(self, mykey):
        return (mykey % self.n)
    def rehashFunction(self, hashkey):
        return (hashkey + 1)% self.n
    def insertData(self, student_obj):
        id = student_obj.getid()
        hashed = self.hashFunction(id)

        while hashed <= self.n:
            if self.hashtable[hashed] is None:
                self.hashtable[hashed] = student_obj
                print('done %d succesfully at %d' %(id, hashed))
                return
            else:
                hashed = self.rehashFunction(hashed)
        print('student %d couldn\'t be inserted.' %id)
    def searchData(self, key):
        hashed = self.hashFunction(key)
        while self.hashtable[hashed] is not None:

            if self.hashtable[hashed].getid() != key:
                hashed = self.rehashFunction(hashed)
            else:
                return self.hashtable[hashed]
class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa
    def getid(self):
        return self.id
    def getName(self):
        return self.name
    def getGpa(self):
        return self.gpa
    def printDetail(self):
        print('ID: %d\nName: %s\nGPA: %f' %(self.id, self.name, self.gpa))

s1 = Student(65070001, "Sandee Boonmak", 3.05) 
s2 = Student(65070077, "SomsakJaidee", 2.78) 
s3 = Student(65070021, "SomsriJaiyai", 3.44) 
s4 = Student(65070042, "SommaiMeeboon", 2.89)

myHash= ProbHash(20) 
myHash.insertData(s1) 
myHash.insertData(s2) 
myHash.insertData(s3) 
myHash.insertData(s4)

std = myHash.searchData(65070077) 
std.printDetail() 
print("-------------------------") 
std = myHash.searchData(65070021) 
std.printDetail() 
print("-------------------------") 
std = myHash.searchData(65070042) 
std.printDetail() 
print("-------------------------") 
std = myHash.searchData(65070032)