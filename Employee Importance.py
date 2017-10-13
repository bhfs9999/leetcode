"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class TreeNone:
    def __init__(self, id, imp):
        self.id = id    
        self.imp = imp
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        res = 0
        for aemp in employees:
            if aemp.id != id:
                continue
            res += aemp.importance
            for aid in aemp.subordinates:
                res += self.getImportance(employees, aid)
            return res
        