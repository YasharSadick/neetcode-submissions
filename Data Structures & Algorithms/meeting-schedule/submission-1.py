"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
      def get_start(intervals):
        return intervals.start
      intervals.sort(key = get_start)
      for i in range (1, len(intervals)):
        previousMeeting = intervals[i -1]
        currentMeeting = intervals[i]
        if previousMeeting.end > currentMeeting.start:
         return False
      return True
    

