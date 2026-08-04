from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals according to their starting value
        intervals.sort(key=lambda interval: interval[0])

        # Add the first interval to the result
        output = [intervals[0]]

        for start, end in intervals[1:]:
            # Ending value of the last interval in output
            last_end = output[-1][1]

            if start <= last_end:
                # The intervals overlap, so extend the ending value
                output[-1][1] = max(last_end, end)
            else:
                # No overlap, so add a new interval
                output.append([start, end])

        return output