from textblob import TextBlob


# Making the text input by the user which has to be analyse
text = input("Enter your text which has to be analyse->")


root = TextBlob(text)


# The output values will be between -1 to +1
# If the number comes as -ive value then the given text is said in negative manner
# If the number comes as +ive value then the given text is said in positive manner
sentiment = root.sentiment.polarity



print(sentiment)


# Writing the conditional statements for the answers
if sentiment<0:
    print("Sentiment is Negative")


elif sentiment>0:
    print("Sentiment is Positive")


elif sentiment==0:
    print("Sentiment is Positive")
