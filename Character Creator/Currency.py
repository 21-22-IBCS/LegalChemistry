from graphics import*
from Button import*


convertion_rates = {"EUR": 0.84,
                   "CNY": 6.36,
                   "HKD": 7.8,
                    "SOS":585,
                    "KGS":84.8,
                    "INS":3.19,
                    }
    
def convert_currency(amount_usd, target_currency):
    # convert usd to target currency
    return amount_usd * convertion_rates[target_currency]

def format_output(output_raw, target_currency):
    # format numeric output into user readable currency amount
    # (84, "EUR") -> "84 EUR"
    return "{:.2f} ".format(output_raw) + target_currency

def format_input(input_raw):
    # format user input into number
    # "123" -> 123
    return int(input_raw)
    
def main():
    win = GraphWin("Currency Converter", 800, 600)
    output_box = Text(Point(450,200), "0.00")
    output_box.draw(win)
    input_box = Entry(Point(450,300),45)
    input_box.draw(win)
    close = Button(win, "grey", "Quit", Point(150, 560), 45)
    EUR = Button(win, "white", "EUR", Point(720, 50), 45)
    SOS = Button(win, "white", "SOS", Point(720, 150), 45)
    KGS = Button(win, "white", "KGS", Point(720, 250), 45)
    HKD = Button(win, "white", "HKD", Point(720, 350), 45)
    CNY = Button(win, "white", "CNY", Point(720, 450), 45)
    INS = Button(win, "white","INS", Point(720, 550), 45)

    current_usd_amount = 0
    result = 0

    m = win.getMouse()
    while True:
        user_input = input_box.getText()
        current_usd_amount = format_input(user_input)
        print(current_usd_amount)
        if close.isClicked(m):
            break
        if EUR.isClicked(m):
            result = convert_currency(current_usd_amount, "EUR")
            formatted = format_output(result, "EUR")
            output_box.setText(formatted)
            break
        if SOS.isClicked(m):
            result = convert_currency(current_usd_amount, "SOS")
            formatted = format_output(result, "SOS")
            output_box.setText(formatted)
            break
        if KGS.isClicked(m):
            result = convert_currency(current_usd_amount, "KGS")
            formatted = format_output(result, "KGS")
            output_box.setText(formatted)
            break
        if HKD.isClicked(m):
            result = convert_currency(current_usd_amount, "HKD")
            formatted = format_output(result, "HKD")
            output_box.setText(formatted)
            break
        if CNY.isClicked(m):
            result = convert_currency(current_usd_amount, "CNY")
            formatted = format_output(result, "CNY")
            output_box.setText(formatted)
            break
        if INS.isClicked(m):
            result = convert_currency(current_usd_amount, "INS")
            formatted = format_output(result, "INS")
            output_box.setText(formatted)
            break
            
    m = win.getMouse()
    win.close()
    
if __name__ == "__main__":
    main()
