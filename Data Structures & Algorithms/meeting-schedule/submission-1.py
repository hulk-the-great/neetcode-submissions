class Solution:
    def canAttendMeetings(self, intervals):
        # Sort meetings according to their starting time
        intervals.sort(key=lambda interval: interval.start)

        for i in range(1, len(intervals)):
            previous_meeting = intervals[i - 1]
            current_meeting = intervals[i]

            # Meetings overlap
            if previous_meeting.end > current_meeting.start:
                return False

        return True