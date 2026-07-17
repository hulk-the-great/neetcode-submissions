from typing import List


class Solution:
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> bool:

        # Map each course to its prerequisite list
        preMap = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            preMap[course].append(prerequisite)

        # Contains courses in the current DFS path
        visitSet = set()

        def dfs(course):
            # Cycle detected
            if course in visitSet:
                return False

            # Course has no prerequisites
            if preMap[course] == []:
                return True

            visitSet.add(course)

            for prerequisite in preMap[course]:
                if not dfs(prerequisite):
                    return False

            visitSet.remove(course)

            # Mark this course as already verified
            preMap[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True