class Solution:
    def isValid(self, s: str) -> bool:
      opened = []
      closetoOpen = {')' : '(' , ']' : '[' , '}' : '{'}
      for char in s:
        if char in closetoOpen:
            if opened and opened[-1] == closetoOpen[char]:
                opened.pop()
            else:
                return False
        else:
            opened.append(char)
      return True if not opened else False