
# Chatbot with Scikit-learn and Flask

## Project Structure

```
chatbot_with_sklearn/
│
├── app.py              # Main application file
├── training_data.txt   # Text file with training data
├── templates/
│   └── index.html      # HTML file for the web interface
├── static/
│   └── style.css       # CSS file for styling
└── screenshots/
    └── screenshot_1.png
    └── screenshot_2.png
```

## How to Run

1. Ensure you have Python installed on your PC. Download it from [python.org](https://www.python.org/).
2. Install the necessary libraries using `pip`:

   ```sh
   pip install flask scikit-learn
   ```

3. Navigate to the project directory and run the Flask app:

   ```sh
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000/` to interact with your chatbot.

## Screenshots

![Chatbot Interface](screenshots/screenshot_1.png)
![Chatbot Interface](screenshots/screenshot_2.png)

## Code Explanation

### app.py

- Initializes a Flask app and sets up routes for the main page and bot responses.
- Loads training data from `training_data.txt`.
- Uses scikit-learn to vectorize the input text and train a Naive Bayes model.
- Defines a function `get_response` to generate bot responses based on user input.

### training_data.txt

- Contains training data with user inputs and corresponding bot responses.

### index.html

- Defines the HTML structure of the chatbot interface.
- Uses jQuery to handle user input and update the chat display dynamically.

### style.css

- Adds styles to make the chat interface look clean and user-friendly.
- Styles user and bot messages differently for clarity.
