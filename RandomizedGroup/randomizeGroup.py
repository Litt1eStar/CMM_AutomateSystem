import pandas as pd

class Student:
    def __init__(self, studentCode, fullName, nickname):
        self.studentCode = studentCode
        self.fullName = fullName
        self.nickname = nickname
        self.mac = 0
        self.window = 0
        
    def __str__(self):
        return f"{self.studentCode} {self.fullName} {self.nickname} | Window : {self.window}, Mac : {self.mac}"

def read_from_file(filename):
    df = pd.read_csv(filename, encoding='utf-8')
    return df

def convertCSVToUsableData():
    df = read_from_file('./studentData.csv')
    rawData = df.values
    students = []

    for i in range(len(rawData)):
        data = rawData[i]
        student = Student(data[0], data[1], data[2])
        students.append(student)

    for i in range(len(students)):
        print(students[i])
    
    return students

def main():
    data = convertCSVToUsableData()
    
    
    
if __name__ == "__main__":
    main()