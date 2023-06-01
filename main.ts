radio.onReceivedNumber(function (receivedNumber) {
    let Time2 = 0
    let Lap = 0
    serial.writeLine("Lap " + ("" + Lap) + " finished at ")
    // Montrer le numero du tour avec le temps totale
    serial.writeNumber(receivedNumber / 1000)
    serial.writeLine(" secondes")
    serial.writeLine("Lap " + ("" + Lap) + " finished in ")
    // Montrer le numero du tour avec le temps du tour
    serial.writeNumber((receivedNumber - Time2) / 1000)
    serial.writeLine(" secondes")
})
radio.setGroup(193)
