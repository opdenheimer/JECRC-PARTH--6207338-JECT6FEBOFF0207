#Hospital Patient Visit Counter
class Solution:

    def department_patient_count(self, visits):
        dept_count = {}
        ## Write your code here & Don't forget to add return keyword

       
        for visit in visits:
            dept = visit["department"]
            dept_count[dept] = dept_count.get(dept, 0) + 1

       
        max_dept = max(dept_count, key=dept_count.get)

        return [dept_count, max_dept]