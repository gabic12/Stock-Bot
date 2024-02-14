import json
import os
import sys

#Function that returns all avaible stock exchanges in the JSON file 
#   jsonData = is expected to be a JSON object  
#   the function returns a list of stockExchange fields
def getAllStockExchanges(jsonData):
    exchanges = []
    for exchange in jsonData:
        exchanges.append(exchange)
    return exchanges

#Function to search a stock exchange within the 'stockExchange' and 'code' fields from the JSON file
#   jsonData = is expected to be a JSON object 
#   searchValue = user input for a stock exchange to be searched
#   the function returns the entire JSON object if it is found, else it returns None
def getStockExchangeByValue(jsonData, searchValue):
    for exchange in jsonData:
        if searchValue.lower() in exchange['stockExchange'].lower() or searchValue.lower() in exchange['code'].lower():
            return exchange
    return None    

#Function to display the top stock for a given stock exchange
#   stockExchange = is expected to be a JSON object
#   the function returns all topStocks for the given stockExchange
def displayTopStocks(stockExchange):
    if stockExchange:
        print(f"\nTop Stocks for {stockExchange['stockExchange']} :")
        for stock in stockExchange['topStocks']:
            print(f"{stock['stockName']}")
    else:
        print("\nStock Exchange not found.")                             

#Function that return the price field of an entered top stock
#   stockExchange = is expected to be a JSON object
#   searchValue = user input for a top stock to be searched
#   the function returns the price field of the entered topStock, otherwise it returns None  
def getTopStockPrice(stockExchange, searchValue):
    if stockExchange:
        for stock in stockExchange['topStocks']:
            if searchValue.lower() in stock['stockName'].lower() or searchValue.lower() in stock['code'].lower():
                return stock['price']
    return None

#Main Menu function is used to return to the main menu when the user wants it
def mainMenu():
    # Use the function getAllStockExchanges to search for and then display the stock exchanges
    allStockExchanges = getAllStockExchanges(data)

    for exchange in allStockExchanges:
        print(f"{exchange['stockExchange']}")

#Top Stock Menu function is used to return back to the top stock list when the users wants it
#   stockExchange = is expected to be a JSON object
def topStockMenu(stockExchange): 
    #Displays all the top stocks based on the given stockExchange, if it is not a valid stockExchange it will exit
    displayTopStocks(stockExchange)

    if not stockExchange:
        return

    #User will input the value for the top stock
    topStockValue = input("\nPlease enter the stock: \n")

    #The price of the entered top stock will be searched, if it is not found a suggestive message will be displayed
    topStockPrice = getTopStockPrice(stockExchange, topStockValue)
    if topStockPrice is not None:
        print(f"\nStock Price of {topStockValue} is {topStockPrice:.2f}")
    else:
        print("\nTop Stock not found.")    

#Function that checks if the file exists, is it empty or it is a valid JSON
#   jsonFile = is expected to be a string containing the name of the file
#   the function returns a tuple containing: a boolean indicating whether the file exists or not, the size of the file in bytes (if the file does not exits it returns 0) 
#                                            and a boolean indicating whether the file is a valid JSON file or not
def checkFile(jsonFile):
    #Checks if the files exists
    fileExists = os.path.exists(jsonFile)

    if fileExists:
        #Calculated the size of the file
        fileSize = os.path.getsize(jsonFile)

        #Checks if the file is  valid JSON
        try:
            with open(jsonFile, 'r') as file:
                json.load(file)
            isJSON = True
        except (json.JSONDecodeError, FileNotFoundError):
            isJSON = False

        return fileExists, fileSize, isJSON
    else:
        return False, 0, False


# Specify the name of the JSON file - change here if the file name modified
jsonFile = 'stockData.json'

#Use the function checkFile to check the file and displays suggestive messages if the file is empty, if the file does not exist or it is not a valid JSON file
#   the user will have the option to exit the application
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


#Start of the Chat Bot
print("Hello! Welcome to LSEG. I'm here to help you.\n")

mainMenu()

exchangeValue = input("\nPlease enter the Stock exchange: \n")  

stockExchange = getStockExchangeByValue(data, exchangeValue)

topStockMenu(stockExchange)

#While loop for a continuous run of the Chat Bot
while True:

    userInput = input("\nDo you want to exit, go back or go to the main menu? \n")

    #Based on user input the chat bot will close, go back to the previous Top Stocks Menu or return to the Main Menu
    if userInput.lower() == "exit" or userInput.lower() == "out" or userInput.lower() == "quit":

        print("\nHave a nice day! :)")

        break

    elif userInput.lower() == "go back" or userInput.lower() == "back":

        topStockMenu(stockExchange)

    elif userInput.lower() == "main menu" or userInput.lower() == "menu" or userInput.lower() == "main":

        mainMenu()

        exchangeValue = input("\nPlease enter the Stock exchange: \n")  

        stockExchange = getStockExchangeByValue(data, exchangeValue)

        topStockMenu(stockExchange)

    else:
        print("\nI didn't understand that. Do you want to exit, go back or go to the main menu? \n")