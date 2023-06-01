def on_received_number(receivedNumber):
    basic.show_string("" + str((receivedNumber)))
radio.on_received_number(on_received_number)

radio.set_group(193)



def on_forever():
    Time2 = 0
    Lap = 0
    serial.write_line("Lap " + ("" + str(Lap)) + " finished at ")
    # Montrer le numero du tour avec le temps totale
    serial.write_number(control.millis() / 1000)
    serial.write_line(" secondes")
    serial.write_line("Lap " + ("" + str(Lap)) + " finished in ")
    # Montrer le numero du tour avec le temps du tour
    serial.write_number((control.millis() - Time2) / 1000)
    serial.write_line(" secondes")
basic.forever(on_forever)
