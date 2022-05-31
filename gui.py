from tkinter import *

root = Tk()
root.title("Currency Converter")

amount_label = Label(root, relief=RIDGE, text="Amount", font=("Arial 24"))
amount_label.grid(column=0, row=1, padx=0, pady=0, ipadx=30)

from_label = Label(root, relief=RIDGE, text="From", font=("Arial 24"))
from_label.grid(column=1, row=1, padx=50, pady=5, ipadx=40)

to_label = Label(root, relief=RIDGE, text="To", font=("Arial 24"))
to_label.grid(column=2, row=1, padx=10, pady=5, ipadx=50)

entry = Entry(root, width=9, borderwidth=5, font=("Arial 24"))
entry.grid(column=0, row=2)
entry.insert(0, 1)

options = ["US Dollar (USD)", "Euro (EUR)", "Japanese Yen (JYN)", "Australian Dollar (AUD)",
    "Canadian Dollar (CAD)", "Swiss Franc (CHF)", "Swiss Krona (SEK)", "Indian Rupee (INR)",
    "Brazilian Real (BRL)", "Egyptian Pound (EGP)"
]

clicked = StringVar()
clicked.set(options[0])

base_currency = OptionMenu(root, clicked, *options)
base_currency.grid(column=1, row=2, ipady=10)

choice = StringVar()
choice.set(options[1])
conversion_currency = OptionMenu(root, choice, *options)
conversion_currency.grid(column=2, row=2, ipady=10)

USD_Conversions = {
    "base" : options[0],
    "US Dollar (USD)": 1,
    "Euro (EUR)": 0.93,
    "Japanese Yen (JYN)": 126.50,
    "Australian Dollar (AUD)": 1.14,
    "Canadian Dollar (CAD)": 1.28,
    "Swiss Franc (CHF)": 0.68,
    "Swiss Krona (SEK)": 6.92,
    "Indian Rupee (INR)": 77.53,
    "Brazilian Real (BRL)": 4.82,
    "Egyptian Pound (EGP)": 18.58
}

EUR_Conversions = {
    "base" : options[1],
    "Euro (EUR)": 1,
    "US Dollar (USD)": 1.07,
    "Japanese Yen (JYN)": 135.84,
    "Australian Dollar (AUD)": 1.51,
    "Canadian Dollar (CAD)": 0.91,
    "Swiss Franc (CHF)": 1.03,
    "Swiss Krona (SEK)": 10.49,
    "Indian Rupee (INR)": 83.17,
    "Brazilian Real (BRL)": 5.16,
    "Egyptian Pound (EGP)": 19.87
}

JYN_Conversions = {
    "base" : options[2],
    "Japanese Yen (JYN)": 1,
    "Euro (EUR)": 0.0074,
    "US Dollar (USD)": 0.0079,
    "Australian Dollar (AUD)": 0.011,
    "Canadian Dollar (CAD)": 0.010,
    "Swiss Franc (CHF)": 0.0076,
    "Swiss Krona (SEK)": 0.077,
    "Indian Rupee (INR)": 0.61,
    "Brazilian Real (BRL)": 0.038,
    "Egyptian Pound (EGP)": 0.15
}

AUD_Conversions = {
    "base" : options[3],
    "Australian Dollar": 1,
    "Euro (EUR)": 0.66,
    "Japanese Yen (JYN)": 89.68,
    "US Dollar (USD)": 0.71,
    "Canadian Dollar (CAD)": 0.91,
    "Swiss Franc (CHF)": 0.68,
    "Swiss Krona (SEK)": 6.92,
    "Indian Rupee (INR)": 54.94,
    "Brazilian Real (BRL)": 3.42,
    "Egyptian Pound (EGP)": 13.14
}

CAD_Conversions = {
    "base" : options[4],
    "Canadian Dollar (CAD)": 1,
    "Euro (EUR)": 0.73,
    "Japanese Yen (JYN)": 98.55,
    "Australian Dollar (AUD)": 1.10,
    "US Dollar (USD)": 0.78,
    "Swiss Franc (CHF)": 0.75,
    "Swiss Krona (SEK)": 7.61,
    "Indian Rupee (INR)": 60.35,
    "Brazilian Real (BRL)": 3.77,
    "Egyptian Pound (EGP)": 14.49
}

CHF_Conversions = {
    "base" : options[5],
    "Swiss Franc (CHF)": 1,
    "Euro (EUR)": 0.97,
    "Japanese Yen (JYN)": 131.79,
    "Australian Dollar (AUD)": 1.47,
    "Canadian Dollar (CAD)": 1.34,
    "US Dollar (USD)": 1.04,
    "Swiss Krona (SEK)": 10.18,
    "Indian Rupee (INR)": 80.69,
    "Brazilian Real (BRL)": 5.04,
    "Egyptian Pound (EGP)": 19.34
}

SEK_Conversions = {
    "base" : options[6],
    "Swiss Krona (SEK)": 1,
    "Euro (EUR)": 0.97,
    "Japanese Yen (JYN)": 131.79,
    "Australian Dollar (AUD)": 1.47,
    "Canadian Dollar (CAD)": 1.34,
    "Swiss Franc (CHF)": 0.75,
    "US Dollar (USD)": 0.78,
    "Indian Rupee (INR)": 60.35,
    "Brazilian Real (BRL)": 0.49,
    "Egyptian Pound (EGP)": 1.87
}

INR_Conversions = {
    "base" : options[7],
    "Indian Rupee (INR)": 1,
    "Euro (EUR)": 0.012,
    "Japanese Yen (JYN)": 1.63,
    "Australian Dollar (AUD)": 0.018,
    "Canadian Dollar (CAD)": 0.017,
    "Swiss Franc (CHF)": 0.012,
    "Swiss Krona (SEK)": 0.13,
    "US Dollar (USD)": 0.013,
    "Brazilian Real (BRL)": 0.062,
    "Egyptian Pound (EGP)": 0.24
}

BRL_Conversions = {
    "base": options[8],
    "Brazilian Real (BRL)": 1,
    "Indian Rupee (INR)": 16.09,
    "Euro (EUR)": 0.19,
    "Japanese Yen (JYN)": 26.35,
    "Australian Dollar (AUD)": 0.29,
    "Canadian Dollar (CAD)": 0.27,
    "Swiss Franc (CHF)": 0.20,
    "Swiss Krona (SEK)": 2.05,
    "US Dollar (USD)": 0.21,
    "Egyptian Pound (EGP)": 3.85
}

EGP_Conversions = {
    "base": options[9],
    "Egyptian Pound (EGP)": 1,
    "Brazilian Real (BRL)": 0.26,
    "Indian Rupee (INR)": 4.17,
    "Euro (EUR)": 0.050,
    "Japanese Yen (JYN)": 6.84,
    "Australian Dollar (AUD)": 0.076,
    "Canadian Dollar (CAD)": 0.069,
    "Swiss Franc (CHF)": 0.052,
    "Swiss Krona (SEK)": 0.53,
    "US Dollar (USD)": 0.054,
}

currencies = [USD_Conversions, EUR_Conversions, JYN_Conversions, AUD_Conversions,
            CAD_Conversions, CHF_Conversions, SEK_Conversions, INR_Conversions,
            BRL_Conversions
]

display = Label(root, font=("Arial 24"), width=30)


def convertCurrency():
    try:
        amount = float(entry.get())
        for currency in currencies:
            if currency["base"] == clicked.get():
                global display
                display.destroy()
                new_currency = amount * currency[choice.get()]
                formatted = "{:.2f}".format(new_currency)
                final_text = str(formatted) + " " + choice.get()
                # global display 
                display = Label(root, text=final_text, font=("Arial 24"), width=30)
                display.grid(column=1, row=3, padx=20)
            else:
                pass
    except:
        display.destroy()
        display = Label(root, text="Invalid Input. Cannot Convert String Characters", font=("Arial 24"))
        display.grid(column=1, row=3)

convert_button = Button(root, text="Convert", command=convertCurrency, font=("Arial 24"), borderwidth=5)
convert_button.grid(column=0, row=3, ipadx=20, pady=10)

root.mainloop()
