class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m = len(num1)
        n = len(num2)

        result = [0]*(m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])

                product = digit1 * digit2

                result[i + j + 1] += product
        for  i in range(m + n - 1, 0, -1):
                result[i - 1] += result[i] // 10
                result[i] %= 10
        answer = "".join(map(str, result))
        return answer.lstrip("0") or "0"