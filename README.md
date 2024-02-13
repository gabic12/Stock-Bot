This is a Chat Bot I created for a LSEG tech challenge. It uses Python to read data from a .JSON file, afterwards it queries the user to select a stock exchange from the provided list and, for the selected exchange, it provides all the stocks that are linked with the chosen exchange. User can then chose a stock and the bot will provide the price of said stock.

Requirements:
 - latest version of Python installed (I have used Python 3.12),
 - an IDE to view the code (I have used Visual Studio Code).

This is a simple bot that runs in the console, so I will set up an improvement plan to be done in the future:
  - add a graphic interface to it to improve user experience,
  - add a natural language functionality, such as Python's nltk,
  - create a database to save the data from the JSON file there and, instead of reading directly from the file, query the database using SQL (this will come in handy when the file will get larger and more complex),
  - publish the bot, so it can be used with external applications such as Microsoft Team or Facebook Messenger.
