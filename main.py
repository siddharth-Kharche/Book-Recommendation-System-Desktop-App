from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load the dataset
def load_books_data():
    return pd.read_csv('books.csv')

df = load_books_data()

# Check if necessary columns exist in the dataset
if 'Title' not in df.columns or 'Genre' not in df.columns:
    raise ValueError("The dataset must contain at least 'Title' and 'Genre' columns.")

# Create a column for recommendation (concatenating Genre if needed)
df['features'] = df['Genre']

# Convert the 'features' (i.e., Genre) into vectors using CountVectorizer
cv = CountVectorizer()
vector_matrix = cv.fit_transform(df['features'])

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(vector_matrix)

# Function to get the index of a book title
def get_index_from_title(title):
    return df[df.Title == title].index.values[0]

# Function to get the title from the index
def get_title_from_index(index):
    return df.iloc[index]['Title']

# Home route for book selection and recommendation
@app.route('/', methods=['GET', 'POST'])
def home():
    recommended_books = []
    
    if request.method == 'POST':
        # Get the selected book from form
        selected_book = request.form.get('book_title')
        
        if selected_book:
            # Get the index of the selected book
            book_index = get_index_from_title(selected_book)
            
            # Get list of similarity scores for the selected book
            similar_books = list(enumerate(cosine_sim[book_index]))
            
            # Sort the books based on similarity scores
            sorted_similar_books = sorted(similar_books, key=lambda x: x[1], reverse=True)[1:6]
            
            # Prepare the top 5 recommended books
            recommended_books = [(get_title_from_index(index), score) for index, score in sorted_similar_books]
    
    # Pass the book titles and recommendations to the template
    return render_template('index.html', books=df['Title'].values, recommended_books=recommended_books)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
