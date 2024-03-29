class Solution:
    def calculate(self, s):

        stack = []
        operand = 0
        output = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative  

        for ch in s:

            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left,
                # with result, sign, operand
                output += sign * operand

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':

                output += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(output)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                output = 0

            elif ch == ')':

                # Evaluate the expression to the left
                # with result, sign and operand
                output += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                output *= stack.pop() # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                output += stack.pop() # stack pop 2, operand

                # Reset the operand
                operand = 0

        output += (sign * operand)

        return output

solution = Solution()

assert(solution.calculate("(1+(4+5+2)-3)+(6+8)") == 23)

print("PASS")