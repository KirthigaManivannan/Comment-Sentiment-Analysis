import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load comments from CSV file
comments_df = pd.read_csv("comments.csv")

# Assuming the column name containing reviews is 'ReviewText', adjust it if different
sentiments = comments_df["ReviewText"].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

# Classify sentiments into positive, neutral, and negative
positive_comments = sum(sentiments > 0)
neutral_comments = sum(sentiments == 0)
negative_comments = sum(sentiments < 0)

# Output with wordings or emojis
print("Sentiment Distribution:")
print(f"Positive: {positive_comments} reviews 😊")
print(f"Neutral: {neutral_comments} reviews 😐")
print(f"Negative: {negative_comments} reviews 😔")

# Plotting
labels = ['Positive', 'Neutral', 'Negative']
sizes = [positive_comments, neutral_comments, negative_comments]
colors = ['#99ff99', '#d3d3d3', '#ff9999']  # Green, Gray, Red

# Pie chart
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Sentiment Distribution')

# Bar chart
plt.subplot(1, 2, 2)
plt.bar(labels, sizes, color=colors)
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')

plt.tight_layout()
plt.show()




















 
   