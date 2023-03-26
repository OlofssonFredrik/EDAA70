import json


class ExamResult:
    def __init__(self,course_code, date, grade_limits:list):
        self.course_code = course_code
        self.date = date
        self.grade_limits = grade_limits
        
        self.result = {}
        
    def grade_from_score(self,score):
        
        if score < self.grade_limits[0]:
            grade = 'U'
            return grade
        elif score < self.grade_limits[1]:
            grade = '3'
            return grade
        elif score < self.grade_limits[2]:
            grade = '4'
            return grade
        else:
            grade = '5'
            return grade
    
    def add_result(self,studentid, score):
        self.result[studentid] = self.grade_from_score(score)
    
    def get_result(self,studentid):
        return self.result[studentid]
    
    def students(self):
        unordered_students = []
        
        for k,v in self.result.items():
            unordered_students.append(k)
            
        unordered_students.sort(key=lambda x: int(x[1:]))
        ordered = unordered_students
        return ordered
            
    def students_highest_score(self):
        sorted_ids = sorted(self.result.keys(), key=lambda x: (
        {'5': 0, '4': 1, '3': 2, 'U': 3}[self.result[x]], x))

        return sorted_ids
    
    def statistics(self):
        grades = ['U', '3', '4', '5']
        grade_counts = {grade: (0, 0) for grade in grades}

        for grade in self.result.values():
            if grade in grade_counts:
                grade_counts[grade] = (grade_counts[grade][0] + 1, 0)

        total_students = len(self.result)
        for grade, count in grade_counts.items():
            grade_counts[grade] = (count[0], count[0] / total_students)

        return grade_counts
        
    
    def print_results(self):
        pass
    

exam = ExamResult('EDAA20','2020-01-01',[30,40,50])

exam.add_result('S02',35)
exam.add_result('S01',25)
exam.add_result('S04',15)
exam.add_result('S03',45)
exam.add_result('S05',55)
print(exam.get_result('S01'))

print(exam.students())

print(exam.students_highest_score())

print(exam.statistics())






print(f"All students results: {json.dumps(exam.result,indent=4)}")

    


