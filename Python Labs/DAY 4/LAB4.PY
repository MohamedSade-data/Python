class subjects:
    def __init__(self, sub_name, passing_grade, student_grade):
            self.passing_grade = passing_grade
            self.name = sub_name
            self.student_grade = student_grade
            
class student:
     def __init__(self, std_name, mail):
           self.name = std_name
           self.mail = mail
           self.list = []
           
     def add_subject(self, sub: subjects):
           if ((type(sub.student_grade) == int or type(sub.student_grade) == float and sub.student_grade > 0)
                and (type(sub.passing_grade) == int or type(sub.passing_grade) == float)):
                self.list.append(sub)

     def Check(self):
        for i in self.list:
            if i.student_grade > i.passing_grade:
                return (f'{self.name} passed in {i.name}')
            else:
                return "failed"

sub1 = subjects("C#", 50, 75.5)
sub2 = subjects("C++", 50, 13)
std = student("Mohamed","Mohamed@icloud.com")
std.add_subject(sub1)

print(std.Check())