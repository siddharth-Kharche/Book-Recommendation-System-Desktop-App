

# Genre-Based Book Recommendation System

This is a **Streamlit** web application that provides book recommendations based on genres using machine learning techniques. The app utilizes the **CountVectorizer** from **Scikit-learn** to convert genres into numerical vectors and then uses **cosine similarity** to recommend books that are similar to the selected book.

## Features

- **Book Recommendations**: Select a book, and the app will recommend the top 5 books based on the genre similarity.
- **Cosine Similarity**: The app uses cosine similarity to find books with the closest genre matches.
- **Integrated Dataset**: The app comes with a pre-loaded CSV file (`books.csv`) containing book titles and genres.

## Demo

You can see a working demo of the app below:

![Book Recommendation App Demo](https://book-recommendation-system-desktop-app.streamlit.app/)

## How it works

1. The user selects a book title from the dropdown list.
2. The app computes similarity between the selected book and all other books based on their genres.
3. It recommends the top 5 books that are most similar to the selected one.

## Dataset

The app uses a CSV file named `books.csv` that contains the following columns:

- **Title**: The title of the book.
- **Genre**: The genre of the book.

Sample data format:

| Title                     | Genre         |
|----------------------------|---------------|
| Harry Potter and the Sorcerer's Stone | Fantasy       |
| The Hobbit                  | Fantasy       |
| The Da Vinci Code           | Mystery       |
| A Brief History of Time     | Science       |

## Technologies Used

- **Streamlit**: For the web interface.
- **Pandas**: To handle data loading and manipulation.
- **Scikit-learn**: To compute cosine similarity using `CountVectorizer`.

## Installation

Follow these steps to set up the app locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/book-recommendation-app.git
   cd book-recommendation-app
   ```

2. **Install the required packages:**
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

4. **Access the app:**
   Once the app is running, open your browser and go to `http://localhost:8501/`.

## Code Overview

### Machine Learning Algorithm

The app uses **CountVectorizer** to convert the 'Genre' column into a vector matrix and calculates the similarity scores using **cosine similarity**. The top 5 books with the highest similarity scores are then displayed as recommendations.

### Key Functions

- `get_index_from_title(title)`: Finds the index of a book by its title.
- `get_title_from_index(index)`: Returns the title of a book from its index.
- `cosine_similarity`: Computes the similarity between all books based on their genres.

## Files in the Repository

- **app.py**: The main application code.
- **books.csv**: The dataset with book titles and genres.
- **requirements.txt**: The list of required packages.
- **README.md**: This documentation file.

## Example Output

- **Selected Book**: Harry Potter and the Sorcerer's Stone
- **Recommended Books**:
  1. The Hobbit (Score: 0.89)
  2. The Fellowship of the Ring (Score: 0.87)
  3. Eragon (Score: 0.86)
  4. The Chronicles of Narnia (Score: 0.85)
  5. The Golden Compass (Score: 0.83)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Let me know if you'd like to add any additional details!
