import json
import os
import sys

#Function to display all stock exchanges
def getAllStockExchanges(jsonData):
    exchanges = []
    for exchange in jsonData:
        exchanges.append(exchange)
    return exchanges

#Function to search a stock exchange based on an entered value
def getStockExchangeByValue(jsonData, searchValue):
    for exchange in jsonData:
        if searchValue.lower() in exchange['stockExchange'].lower() or searchValue.lower() in exchange['code'].lower():
            return exchange
    return None    

#Function to display the top stocks for a given stockExchange
def displayTopStocks(stockExchange):
    if stockExchange:
        print(f"\nTop Stocks for {stockExchange['stockExchange']} :")
        for stock in stockExchange['topStocks']:
            print(f"{stock['stockName']}")
    else:
        print("\nStock Exchange not found.")                             

#Function that gets the price of an entered top stock
def getTopStockPrice(stockExchange, searchValue):
    if stockExchange:
        for stock in stockExchange['topStocks']:
            if searchValue.lower() in stock['stockName'].lower() or searchValue.lower() in stock['code'].lower():
                return stock['price']
    return None

#"Main Menu" function
def mainMenu():
    # Use the functions to search for and display the stock exchange
    allStockExchanges = getAllStockExchanges(data)

    for exchange in allStockExchanges:
        print(f"{exchange['stockExchange']}")

#"Top Stock Menu" function
def topStockMenu(stockExchange): 
    displayTopStocks(stockExchange)

    if not stockExchange:
        return

    topStockValue = input("\nPlease enter the stock: ")

    topStockPrice = getTopStockPrice(stockExchange, topStockValue)
    if topStockPrice is not None:
        print(f"\nStock Price of {topStockValue} is {topStockPrice:.2f}")
    else:
        print("\nTop Stock not found.")    

#Function that checks if the file exists, is it empty or it is a valid JSON
def checkFile(jsonFile):
    fileExists = os.path.exists(jsonFile)

    if fileExists:
        fileSize = os.path.getsize(jsonFile)

        try:
            with open(jsonFile, 'r') as file:
                json.load(file)
            isJSON = True
        except (json.JSONDecodeError, FileNotFoundError):
            isJSON = False

        return fileExists, fileSize, isJSON
    else:
        return False, 0, False


# Specify the path to your JSON file - replace with the actual path to your JSON file
jsonFile = 'stockData.json'

#Check the file
fileExists, fileSize, isJSON = checkFile(jsonFile)

if fileExists:
    if fileSize == 0:
        input("The stock file is empty. Press any key to exit.")
        sys.exit()
    elif not isJSON:
        input("The stock file is not a valid JSON file. Press any key to exit.")
        sys.exit()
else:
    input("The stock file does not exist. Press any key to exit.")
    sys.exit()


#Open the file and load the JSON data if the file check passed
with open(jsonFile, 'r') as file:
    data = json.load(file)


#Start of the "Chat Bot"
print("Hello! Welcome to LSEG. I'm here to help you.\n")

mainMenu()

exchangeValue = input("\nPlease enter the Stock exchange: ")  

stockExchange = getStockExchangeByValue(data, exchangeValue)

topStockMenu(stockExchange)

#While loop for a continuous run of the "Chat Bot"
while True:

    userInput = input("\nDo you want to exit, go back or go to the main menu?")

    if userInput.lower() == "exit":

        print("\nHave a nice day! :)")

        break

    elif userInput.lower() == "go back":

        topStockMenu(stockExchange)

    elif userInput.lower() == "main menu":

        mainMenu()

        exchangeValue = input("\nPlease enter the Stock exchange: ")  

        stockExchange = getStockExchangeByValue(data, exchangeValue)

        topStockMenu(stockExchange)

    else:
        print("\nI didn't understand. Do you want to exit, go back or go to the main menu?")