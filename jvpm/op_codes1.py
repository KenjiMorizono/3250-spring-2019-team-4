'''
All Methods for OP Codes go in this file
'''

class op_codes:
        def op_code70(stack_z):     #remainder
                var1 = stack_z.pop() % stack_z.pop()
                stack_z.append(var1)
                return stack_z

        def op_code78(stack_z):     #shift left
                var1 = stack_z.pop() << stack_z.pop()
                stack_z.append(var1)
                return stack_z

        def op_code80(stack_z):     #bitwise OR
                var1 = stack_z.pop() | stack_z.pop()
                stack_z.append(var1)
                return stack_z

        def op_code05(stack_z):        #loads 2 onto stack
                stack_z.append(2)
                return stack_z

        def op_code06(stack_z):        #loads 3 onto stack
                stack_z.append(3)
                return stack_z

        def op_code07(stack_z):        #loads 4 onto stack
                stack_z.append(4)
                return stack_z

        def op_code08(stack_z):        #loads 5 onto stack
                stack_z.append(5)
                return stack_z

        def op_code60(stack_z): # add
                var1 = stack_z.pop() + stack_z.pop()
                stack_z.append(var1)
                return stack_z

        def op_code7e(stack_z): # bitwise and
                var1 = stack_z.pop() & stack_z.pop()
                stack_z.append(var1)
                return stack_z

        def op_code6c(stack_z): # integer division
                var1 = stack_z.pop() / stack_z.pop()
                stack_z.append(var1)
                return stack_z

        def op_code68(stack_z): # multiplication
                var1 = stack_z.pop() * stack_z.pop()
                stack_z.append(var1)
                return stack_z

        def op_codes74(stack_z): # change to negative
                var1 = stack_z.pop() * -1
                stack_z.append(var1)
                return stack_z

