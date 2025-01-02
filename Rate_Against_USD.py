import requests
from bs4 import BeautifulSoup

#Return a vector of tuple with the exchange rate for the currency code given. Ex: [('MXN', '20.6048'),...]
def exchangeRateAgainstUSD(currencyCodes):
    exchangeRatesResult = []

    for currencyCode in currencyCodes:
        exchangeRateURL = "https://www.google.com/finance/quote/USD-" + currencyCode
        responseFromExchangeRate = requests.get(exchangeRateURL)

        if responseFromExchangeRate.ok:
            soup = BeautifulSoup(responseFromExchangeRate.content, "html.parser")
            exchangeRateElement = soup.find('div', class_='YMlKec fxKbKc') # Accessing specific div elements that contains the rate value using class ID

            try:
                exchangeRate = exchangeRateElement.text
                exchangeRatesResult.append((currencyCode, exchangeRate))
            except:
                print("Failed to fetch the webpage. Error: ", responseFromExchangeRate.status_code)

    return exchangeRatesResult

def main():
    currencyCodes = ["MXN", "ARS", "CAD"]
    exchangeRatesResult = exchangeRateAgainstUSD(currencyCodes)

    print(exchangeRatesResult)

if __name__ == '__main__':
    main()