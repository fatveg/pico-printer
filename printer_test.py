import machine
from epson_thermal import ThermalPrinter

# seutup uart for printer
uart = machine.UART(0, 9600, tx=machine.Pin(0), rx=machine.Pin(1))

# create printer object
printer = ThermalPrinter(uart)

# print text
printer.add_text("Hello World")
# printer.add_bytes(b"\x1D\x21\x33", feed=0)
printer.set_magnification(3, 1)
printer.add_text("Hello World 2")
printer.set_magnification(1, 2)
printer.add_text("Hello World 3")
printer.set_magnification()
printer.add_text("Hello World 4")


# print buffer
printer.write_buffer()
