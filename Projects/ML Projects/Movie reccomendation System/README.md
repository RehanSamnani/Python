# Movie Recommendation System

## Required Libraries
To run this project, you need to install the following libraries:

- numpy
- pandas
- matplotlib
- scikit-learn
- nltk
- streamlit

You can install these libraries using the following command:
```bash
pip install numpy pandas matplotlib scikit-learn nltk streamlit
```

## Demo View
This project is a movie recommendation system that suggests movies based on user input. The interface is built using Streamlit, and the recommendations are generated using cosine similarity on movie tags. The application has a Netflix-like theme for an engaging user experience.

Below is a screenshot of the application:

![Movie Recommendation System](attachments/demo_view.png)

## Steps to Build the Application

### 1. Data Collection
- Use the TMDb 5000 Movies and Credits dataset.
- Load the datasets using pandas.

### 2. Data Cleaning
- Merge the movies and credits datasets on the `title` column.
- Select relevant columns: `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, and `crew`.
- Handle missing values by dropping rows with null values.

### 3. Feature Engineering
- Create a `tags` column by combining `overview`, `genres`, `keywords`, `cast`, and `crew`.
- Convert text to lowercase and remove spaces.

### 4. Text Preprocessing
- Use the `nltk` library to apply stemming to the `tags` column.

### 5. Vectorization
- Convert the `tags` column into vectors using `CountVectorizer` from `scikit-learn`.
- Limit the vocabulary to the top 5000 words and remove stop words.

### 6. Similarity Calculation
- Compute cosine similarity between movie vectors using `cosine_similarity` from `scikit-learn`.
- Save the similarity matrix to a `.npy` file for later use.

### 7. Recommendation Function
- Create a function to recommend movies based on the similarity matrix.
- The function takes a movie title as input and returns the top 5 similar movies.

### 8. Web Interface
- Build a user-friendly interface using Streamlit.
- Allow users to select a movie from a dropdown menu and display recommendations with posters.

### 9. Styling
- Add custom CSS to give the application a Netflix-like theme.

## How to Run the Application
1. Clone the repository.
2. Install the required libraries.
3. Run the Streamlit application using the following command:
   ```bash
   streamlit run app.py
   ```
4. Open the application in your browser and enjoy movie recommendations!