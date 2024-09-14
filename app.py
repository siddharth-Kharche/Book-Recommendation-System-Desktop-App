import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Title of the app
st.title('Book Recommendation System')

# Load the dataset from the backend (local CSV file)
@st.cache_data
def load_books_data():
    return pd.read_csv('books.csv')

# Load books.csv directly from the path
df = load_books_data()

# Display the first few rows of the dataset to the user


# Check if necessary columns exist in the dataset
if 'Title' not in df.columns or 'Genre' not in df.columns:
    st.error("The dataset must contain at least 'Title' and 'Genre' columns.")
else:
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
    
    # User selects a book title
    book_title = st.selectbox('Select a book title', df['Title'].values)

    if book_title:
        st.write(f'**Selected Book:** {book_title}')
        
        # Get the index of the selected book
        book_index = get_index_from_title(book_title)
        
        # Get list of similarity scores for the selected book
        similar_books = list(enumerate(cosine_sim[book_index]))
        
        # Sort the books based on similarity scores
        sorted_similar_books = sorted(similar_books, key=lambda x: x[1], reverse=True)[1:6]
        
        st.write('**Top 5 recommended books based on Genre:**')
        
        # Display the top 5 recommended books
        for i, (index, score) in enumerate(sorted_similar_books):
            st.write(f"{i+1}. {get_title_from_index(index)} (Score: {score:.2f})")

# Run the app using `streamlit run your_file.py`
