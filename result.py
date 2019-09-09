from operation_type import Operation

class Result:
    def get_typed_message(self, op):
        return 'Encoded' if op == Operation.ENCODE else 'Decoded'

    def __init__(self, op, msg):
        self.type_message = self.get_typed_message(op)
        self.msg = msg

