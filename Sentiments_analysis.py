from textblob import TextBlob

text = input("Enter your text which has to be analyse->")


root = TextBlob(text)


sentiment = root.sentiment.polarity



print(sentiment)


if sentiment<0:
    print("Sentiment is Negative")


elif sentiment>0:
    print("Sentiment is Positive")


elif sentiment==0:
    print("Sentiment is Positive")
