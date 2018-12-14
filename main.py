import wasmi
import wasmi.interpreter
import wasmi.leb128

code = [0x00, 0x61, 0x73, 0x6d, 0x01, 0x00, 0x00, 0x00,
        0x01, 0x07, 0x01, 0x60, 0x02, 0x7f, 0x7f, 0x01,
        0x7f, 0x03, 0x02, 0x01, 0x00, 0x07, 0x07, 0x01,
        0x03, 0x61, 0x64, 0x64, 0x00, 0x00, 0x0a, 0x09,
        0x01, 0x07, 0x00, 0x20, 0x00, 0x20, 0x01, 0x6a,
        0x0f, 0x0b]

data = [0x00, 0x00, 0x00, 0x05, 0x00, 0x00, 0x00, 0x02]

it = wasmi.interpreter.Interpreter(bytearray(code))
r = it.exec('add', data)
print(r)
