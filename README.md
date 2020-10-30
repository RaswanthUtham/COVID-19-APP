# COVID-19-APP

## Dependencies (install the below modules)s

    scrapy
    scrapy-user-agents
    pywin32 (for windows)
    SpeechRecognition
    pyttsx3
    pyaudio (use this below link if pip didn't work)
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

## Project Definition

    corona bot will wait for user to ask questions, converts it from speech to text, processes it and gives the answer.
    example:
        user:
            (asks) how many people died due to corona in India
        app: 
            (will read out the data) 1 lakh people died
    how it works:  
        got the input data from web through scrapy framework
        used speechrecognition and pyttsx3 to get input and read the output to user
        
## update in database:
        user:
            update the data
        app:
            will crawl for the latest data from web and stores it in sqlite3 database 
