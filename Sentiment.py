from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
 
from tkinter import *
 
def clearAll() : 
   
    negativeField.delete(0, END) 
    neutralField.delete(0, END) 
    positiveField.delete(0, END) 
    overallField.delete(0, END) 
 
    textArea.delete(1.0, END)
     

def detect_sentiment():
 
    sentence = textArea.get("1.0", "end")
 
     
    sid_obj = SentimentIntensityAnalyzer() 
 

    sentiment_dict = sid_obj.polarity_scores(sentence) 
 
    string = str(sentiment_dict['neg']*100) + "% Negative"
    negativeField.insert(10, string)
     
 
    string = str(sentiment_dict['neu']*100) + "% Neutral"
    neutralField.insert(10, string)
 
    string = str(sentiment_dict['pos']*100) +"% Positive"
    positiveField.insert(10, string)
     
    if sentiment_dict['compound'] >= 0.05 :
        string = "Positive"
 
    elif sentiment_dict['compound'] <= - 0.05 :
        string = "Negative"
      
 
    else :
        string = "Neutral"
 
    overallField.insert(10, string)
         
 

if __name__ == "__main__" :
     
    gui = Tk() 
     
    gui.config(background =  "light grey") 
 
    gui.title("Sentiment Detector") 
 
    gui.geometry("400x700")
    gui.resizable(0,0) 
 
    enterText = Label(gui, text = "Enter Your Sentence", font= "lucida 16")
 
 
    textArea = Text(gui, height = 5, width = 30, font = "lucida 16")
 
  
    check = Button(gui, text = "Check Sentiment", fg = "Black", command = detect_sentiment, font = "lucida 16")
 
    negative = Label(gui, text = "sentence was rated as: ", font = "lucida 16")
   
    neutral = Label(gui, text = "sentence was rated as: ", font = "lucida 16")
   
    positive = Label(gui, text = "sentence was rated as: ", font = "lucida 16")
 
    overall = Label(gui, text = "Sentence Overall Rated As: ", font = "lucida 16")
  
    negativeField = Entry(gui, font = "lucida 14")
  
    neutralField = Entry(gui, font = "lucida 14")
  
    positiveField = Entry(gui, font = "lucida 14")
  
    overallField = Entry(gui, font = "lucida 14") 
 
 
    clear = Button(gui, text = "Clear", fg = "Black", command = clearAll, font = "lucida 16")
     

    Exit = Button(gui, text = "Exit", fg = "Black", command = exit, font = "lucida 16")

    enterText.grid(row = 1, column = 2, padx=10, pady=10)
     
    textArea.grid(row = 2, column = 2, padx = 10, sticky = W)
     
    check.grid(row = 3, column = 2, padx=10, pady=10)
     
    negative.grid(row = 4, column = 2, padx=10, pady=10)
     
    neutral.grid(row = 6, column = 2, padx=10, pady=10)
     
    positive.grid(row = 8, column = 2, padx=10, pady=10)
     
    overall.grid(row = 10, column = 2, padx=10, pady=10)
     
    negativeField.grid(row = 5, column = 2)
 
    neutralField.grid(row = 7, column = 2)
                       
    positiveField.grid(row = 9, column = 2)
     
    overallField.grid(row = 11, column = 2)
     
    clear.grid(row = 12, column = 2, padx=10, pady=10)
     
    Exit.grid(row = 13, column = 2, padx=10, pady=10)
 

    gui.mainloop() 
    