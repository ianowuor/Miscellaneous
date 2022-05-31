print("CURRENCY CONVERTER")
print()
print("Common Currencies")
print()
print("Currency Name      Currency Code")
print()
print("US Dollar          USD")
print("Euro               EUR")
print("Japaneese Yen      JYN")
print("Australian Dollar  AUD")
print("Canadian Dollar    CAD")
print("Swiss Frank        CHF")
print("Swedish Krona      SEK")
print("Indian Rupee       INR")

currency_codes = ["USD", "EUR", "JYN", "AUD", "CAD", "CHF", "SEK", "INR"]

base_currency_code = input("Enter Currency Code: ")
while(base_currency_code not in currency_codes):
    print("Currency Code does not exist. Input the correct currency code")
    base_currency_code = input("Enter Currency Code: ")

conversion_currency_code = input(f"Enter currency code to be converted from {base_currency_code}: ")
while(conversion_currency_code == base_currency_code or conversion_currency_code not in currency_codes):
    if conversion_currency_code == base_currency_code:
        print(f"You cannot convert {base_currency_code} to {conversion_currency_code}")
    else:
        print("Currency Code does not exist. Input the correct currency code")

    conversion_currency_code = input(f"Enter currency code to be converted from {base_currency_code}: ")

USD_Conversions = {
    "base" : "USD",
    "EUR": 0.93,
    "JYN": 126.50,
    "AUD": 1.14,
    "CAD": 1.28,
    "CHF": 0.68,
    "SEK": 6.92,
    "INR": 77.53
}

EUR_Conversions = {
    "base" : "EUR",
    "USD": 1.07,
    "JYN": 135.84,
    "AUD": 1.51,
    "CAD": 0.91,
    "CHF": 1.03,
    "SEK": 10.49,
    "INR": 83.17
}

JYN_Conversions = {
    "base" : "JYN",
    "EUR": 0.0074,
    "USD": 0.0079,
    "AUD": 0.011,
    "CAD": 0.010,
    "CHF": 0.0076,
    "SEK": 0.077,
    "INR": 0.61
}

AUD_Conversions = {
    "base" : "AUD",
    "EUR": 0.66,
    "JYN": 89.68,
    "USD": 0.71,
    "CAD": 0.91,
    "CHF": 0.68,
    "SEK": 6.92,
    "INR": 54.94
}

CAD_Conversions = {
    "base" : "CAD",
    "EUR": 0.73,
    "JYN": 98.55,
    "AUD": 1.10,
    "USD": 0.78,
    "CHF": 0.75,
    "SEK": 7.61,
    "INR": 60.35
}

CHF_Conversions = {
    "base" : "CHF",
    "EUR": 0.97,
    "JYN": 131.79,
    "AUD": 1.47,
    "CAD": 1.34,
    "USD": 1.04,
    "SEK": 10.18,
    "INR": 80.69
}

SEK_Conversions = {
    "base" : "SEK",
    "EUR": 0.97,
    "JYN": 131.79,
    "AUD": 1.47,
    "CAD": 1.34,
    "CHF": 0.75,
    "USD": 0.78,
    "INR": 60.35
}

INR_Conversions = {
    "base" : "INR",
    "EUR": 0.012,
    "JYN": 1.63,
    "AUD": 0.018,
    "CAD": 0.017,
    "CHF": 0.012,
    "SEK": 0.13,
    "USD": 0.013
}

currency_code_conversions = [USD_Conversions, EUR_Conversions, JYN_Conversions, AUD_Conversions, CAD_Conversions, CHF_Conversions, SEK_Conversions, INR_Conversions]
convert_currency = True

while convert_currency:
    amount_to_convert = float(input(f"Enter amount of {base_currency_code} to convert to {conversion_currency_code}: "))
    converted_currency = 0
    for conversion in currency_code_conversions:
        if conversion["base"] == base_currency_code:
            converted_currency = amount_to_convert * conversion[conversion_currency_code]
            break
        else:
            pass

    print(f"{amount_to_convert} {base_currency_code} = {converted_currency} {conversion_currency_code}")
    print("To continue converting currencies, input YES")
    choice = input("Do you want to continue converting currencies? : ")
    if choice == "YES" or choice == "yes":
        base_currency_code = input("Enter Currency Code: ")
        while(base_currency_code not in currency_codes):
            print("Currency Code does not exist. Input the correct currency code")
            base_currency_code = input("Enter Currency Code: ")

        conversion_currency_code = input(f"Enter currency code to be converted from {base_currency_code}: ")
        while(conversion_currency_code == base_currency_code or conversion_currency_code not in currency_codes):
            if conversion_currency_code == base_currency_code:
                print(f"You cannot convert {base_currency_code} to {conversion_currency_code}")
            else:
                print("Currency Code does not exist. Input the correct currency code")

            conversion_currency_code = input(f"Enter currency code to be converted from {base_currency_code}: ")
    else:
        print("Thanks for using Currency Converter")
        convert_currency = False