import unittest
from jvpm import op_codes1

class test_op_codes(unittest.TestCase):

    """
    def test_opcodeb6(self):    # TODO Make better tests as invokevirtual can call a variety of methods
        test_stack = []
        test_input = 1337
        test_call_path = ["java/util/Scanner", "nextInt", "()I"]
        operator = op_codes1.op_codes()

        operator.invokevirtual(test_stack, test_call_path)

        @unittest.patch('builtins.input', return_value = test_input)
        def test_nextInt(self, input):
            self.assertEqual(test_stack.pop(), 1337)
    """

    def test_iconst_2(self): #load 2 onto stack
        test_stack = [1, 2]
        test_stack = op_codes1.op_codes.iconst_2(test_stack)
        self.assertEqual(test_stack.pop(), 2)

    def test_iconst_3(self): #load 3 onto stack
        test_stack = [1, 2]
        test_stack = op_codes1.op_codes.iconst_3(test_stack)
        self.assertEqual(test_stack.pop(), 3)

    def test_iconst_4(self): #load 4 onto stack
        test_stack = [1, 2]
        test_stack = op_codes1.op_codes.iconst_4(test_stack)
        self.assertEqual(test_stack.pop(), 4)

    def test_iconst_5(self): #load 5 onto stack
        test_stack = [1, 2]
        test_stack = op_codes1.op_codes.iconst_5(test_stack)
        self.assertEqual(test_stack.pop(), 5)

    def test_irem(self): # remainder
        test_stack = [1, 2]
        test_stack = op_codes1.op_codes.irem(test_stack)
        self.assertEqual(test_stack.pop() , 0)

    def test_ishl(self): # shift left
        test_stack = [1, 2]
        test_stack = op_codes1.op_codes.ishl(test_stack)
        self.assertEqual(test_stack.pop() , 4)

    def test_iushr(self): #shift right
        test_stack = [1, 2]
        test_stack = op_codes1.op_codes.iushr(test_stack)
        self.assertEqual(test_stack.pop() , 1)

    def test_ishr(self):  # arithmetic shift right
        test_stack = [2, 15]
        operator = op_codes1.op_codes()
        operator.ishr(test_stack)

        self.assertEqual(test_stack.pop(), 3)

    def test_ixor(self): #bitwise XOR
        test_stack = [1, 2]
        test_stack = op_codes1.op_codes.ixor(test_stack)
        self.assertEqual(test_stack.pop() , 3)

    def test_ior(self): # bitwise OR
        test_stack = [1, 2]
        test_stack = op_codes1.op_codes.ior(test_stack)
        self.assertEqual(test_stack.pop() , 3)


    def test_iadd(self): # add
        test_stack = [1, 2, 2147483647, 2147483647, -2147483647, -2147483647]
        test_stack = op_codes1.op_codes.iadd(test_stack)
        self.assertEqual(test_stack.pop(), -2147483647)
        test_stack = op_codes1.op_codes.iadd(test_stack)
        self.assertEqual(test_stack.pop(), 2147483647)
        test_stack = op_codes1.op_codes.iadd(test_stack)
        self.assertEqual(test_stack.pop(), 3)

    def test_isub(self):  # subtract
        test_stack = [2, 3]
        operator = op_codes1.op_codes()
        operator.isub(test_stack)

        self.assertEqual(test_stack.pop(), 1)

    def test_iand(self): # bitwise AND
        test_stack = [1, 2]
        test_stack = op_codes1.op_codes.iand(test_stack)
        self.assertEqual(test_stack.pop(), 1&2)

    def test_idiv(self): # integer division
        test_stack = [1, 2, 2, 0]
        self.assertRaises(ArithmeticError, test_stack = op_codes1.op_codes.idiv(test_stack))
        test_stack = op_codes1.op_codes.idiv(test_stack)
        self.assertEqual(test_stack.pop(), 1 // 2)

    def test_imul(self): # multiplication
        test_stack = [1, 2, 2147483647, 2147483647, 2147483647, 4, 2147483647, 5, -2147483647, -2147483647, -2147483647, 4, -2147483647, 5]
        test_stack = op_codes1.op_codes.imul(test_stack)
        self.assertEqual(test_stack.pop(), -2147483647)
        test_stack = op_codes1.op_codes.imul(test_stack)
        self.assertEqual(test_stack.pop(), 0)
        test_stack = op_codes1.op_codes.imul(test_stack)
        self.assertEqual(test_stack.pop(), 0)
        test_stack = op_codes1.op_codes.imul(test_stack)
        self.assertEqual(test_stack.pop(), 2147483643)
        test_stack = op_codes1.op_codes.imul(test_stack)
        self.assertEqual(test_stack.pop(), -4)
        test_stack = op_codes1.op_codes.imul(test_stack)
        self.assertEqual(test_stack.pop(), 1)
        test_stack = op_codes1.op_codes.imul(test_stack)
        self.assertEqual(test_stack.pop(), 1 * 2)

    def test_ineg(self): # negative
        test_stack = [1, 2]
        test_stack = op_codes1.op_codes.ineg(test_stack)
        self.assertEqual(test_stack.pop() , -1 * 2)

    def test_iconst_m1(self): #load -1 onto stack
        test_stack = [1, 2]
        test_stack = op_codes1.op_codes.iconst_m1(test_stack)
        self.assertEqual(test_stack.pop(), -1)

    def test_iconst_0(self): #load 0 onto stack
        test_stack = [1, 2]
        test_stack = op_codes1.op_codes.iconst_0(test_stack)
        self.assertEqual(test_stack.pop(), 0)

    def test_iconst_1(self): #load 1 onto stack
        test_stack = []
        test_stack = op_codes1.op_codes.iconst_1(test_stack)
        self.assertEqual(test_stack.pop(), 1)

    #def test_i2b(self): #convert int to byte
    #    test_stack = [1, 2, 2147483647, -214748367, 500, -500, 256, -256, 768, 770]
    #    test_stack = op_codes1.op_codes.i2b(test_stack)
    #    self.assertEqual(test_stack.pop(), bytes([254]))
    #    test_stack = op_codes1.op_codes.i2b(test_stack)
    #    self.assertEqual(test_stack.pop(), bytes([0]))
    #    test_stack = op_codes1.op_codes.i2b(test_stack)
    #    self.assertEqual(test_stack.pop(), bytes([0]))
    #    test_stack = op_codes1.op_codes.i2b(test_stack)
    #    self.assertEqual(test_stack.pop(), bytes([0]))
    #    test_stack = op_codes1.op_codes.i2b(test_stack)
    #    self.assertEqual(test_stack.pop(), bytes([12]))
    #    test_stack = op_codes1.op_codes.i2b(test_stack)
    #    self.assertEqual(test_stack.pop(), bytearray([256-12]))
    #    test_stack = op_codes1.op_codes.i2b(test_stack)
    #    self.assertEqual(test_stack.pop(), bytes([0]))
    #    test_stack = op_codes1.op_codes.i2b(test_stack)
    #    self.assertEqual(test_stack.pop(), bytes([-1]))
    #    test_stack = op_codes1.op_codes.i2b(test_stack)
    #    self.assertEqual(test_stack.pop(), bytes([2]))
    #    test_stack = op_codes1.op_codes.i2b(test_stack)
    #    self.assertEqual(test_stack.pop(), bytes([1]))

    def test_i2c(self):
        test_stack = [-100, 65, 75, 90, 97, 100, 122]
        test_stack = op_codes1.op_codes.i2c(test_stack)
        self.assertEqual(test_stack.pop(), 'z')
        test_stack = op_codes1.op_codes.i2c(test_stack)
        self.assertEqual(test_stack.pop(), 'd')
        test_stack = op_codes1.op_codes.i2c(test_stack)
        self.assertEqual(test_stack.pop(), 'a')
        test_stack = op_codes1.op_codes.i2c(test_stack)
        self.assertEqual(test_stack.pop(), 'Z')
        test_stack = op_codes1.op_codes.i2c(test_stack)
        self.assertEqual(test_stack.pop(), 'K')
        test_stack = op_codes1.op_codes.i2c(test_stack)
        self.assertEqual(test_stack.pop(), 'A')
        test_stack = op_codes1.op_codes.i2c(test_stack)
        self.assertEqual(test_stack.pop(), '?')

    def test_opcode87(self):
        test_stack = [-100, 65, 75, 90]
        test_stack = op_codes1.op_codes.i2d(test_stack)
        self.assertEqual(test_stack.pop(), 90.0)
        test_stack = op_codes1.op_codes.i2d(test_stack)
        self.assertEqual(test_stack.pop(), 75.0)
        test_stack = op_codes1.op_codes.i2d(test_stack)
        self.assertEqual(test_stack.pop(), 65.0)
        test_stack = op_codes1.op_codes.i2d(test_stack)
        self.assertEqual(test_stack.pop(), -100.0)

    def test_i2f(self):
        test_stack = [-100, 65, 75, 90]
        test_stack = op_codes1.op_codes.i2f(test_stack)
        self.assertEqual(test_stack.pop(), 90.0)
        test_stack = op_codes1.op_codes.i2f(test_stack)
        self.assertEqual(test_stack.pop(), 75.0)
        test_stack = op_codes1.op_codes.i2f(test_stack)
        self.assertEqual(test_stack.pop(), 65.0)
        test_stack = op_codes1.op_codes.i2f(test_stack)
        self.assertEqual(test_stack.pop(), -100.0)

    def test_i2l(self):
        test_stack = [2147483647, -2147483647]
        test_stack = op_codes1.op_codes.i2l(test_stack)
        self.assertEqual(test_stack.pop(), -2147483647)
        test_stack = op_codes1.op_codes.i2l(test_stack)
        self.assertEqual(test_stack.pop(), 2147483647)

    def test_iload_0(self):
        test_stack = []
        test_localvar = [20]
        test_stack = op_codes1.op_codes.iload_0(test_stack, test_localvar)
        self.assertEqual(test_stack.pop(), 20)

    def test_iload_1(self):
        test_stack = []
        test_localvar = [20, 10]
        test_stack = op_codes1.op_codes.iload_1(test_stack, test_localvar)
        self.assertEqual(test_stack.pop(), 10)

    def test_iload_2(self):
        test_stack = []
        test_localvar = [20, 10, 5]
        test_stack = op_codes1.op_codes.iload_2(test_stack, test_localvar)
        self.assertEqual(test_stack.pop(), 5)

    def test_iload_3(self):
        test_stack = []
        test_localvar = [20, 5, 8, 9]
        test_stack = op_codes1.op_codes.iload_3(test_stack, test_localvar)
        self.assertEqual(test_stack.pop(), 9)

    def test_iload(self):
        test_stack = []
        test_localvar = [20, 5, 8, 9]
        test_stack = op_codes1.op_codes.iload(test_stack, test_localvar, 2)
        self.assertEqual(test_stack.pop(), 8)
        test_stack = op_codes1.op_codes.iload(test_stack, test_localvar, 0)
        self.assertEqual(test_stack.pop(), 20)

    def test_i2s(self):
        test_stack = [2147483647, -2147483647, 32768, -32770]
        test_stack = op_codes1.op_codes.i2s(test_stack)
        self.assertEqual(test_stack.pop(), 32766)
        test_stack = op_codes1.op_codes.i2s(test_stack)
        self.assertEqual(test_stack.pop(), -32768)
        test_stack = op_codes1.op_codes.i2s(test_stack)
        self.assertEqual(test_stack.pop(), 0)
        test_stack = op_codes1.op_codes.i2s(test_stack)
        self.assertEqual(test_stack.pop(), -1)

    def test_iaload(self):
        test_stack = []
        test_array = [2147483647, -2147483647, 32768, -32770]
        index = 2
        test_stack = op_codes1.op_codes.iaload(test_array, index)
        self.assertEqual(test_stack.pop(), 32768)
