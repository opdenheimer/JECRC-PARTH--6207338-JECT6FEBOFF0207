#Student Marks Performance Tracker
class Solution:

    def subject_average(self, students):
        totals = {}
        count = {}
        n=len(students)
        ## Write your code here and don't forget to add return keyword
        for student in students:
            for subject, marks in student["marks"].items():
                totals[subject] = totals.get(subject, 0) + marks

        
        subject_avg = {}
        for subject in totals:
            subject_avg[subject] = totals[subject] / n

        highest_subject = max(subject_avg, key=subject_avg.get)

        
        return [subject_avg, highest_subject]