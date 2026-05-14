# Imports
import pickle
import numpy as np
import pandas as pd
from flask import Flask, render_template, request

# Creating the App
app = Flask(__name__)

# Function to load the model or the scaler
def load_file(path):
    with open(path, 'rb') as file:
        return pickle.load(file)

# Loading the model and the scaler
model = load_file('final_model.pkl')
scaler = load_file('final_scaler.pkl')

# Route to web home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to predict function
@app.route('/predict', methods=['POST'])
def predict():
    
    try:
        # Extracting all values and send them to form
        english_test = float(request.form.get('english_test', 0))
        psico_exam = int(request.form.get('psico_exam', 0))
        iq_grade = int(request.form.get('iq_grade', 0))

        # Input validation
        if not (0 <= english_test <= 10 and 0 <= iq_grade <= 200 and 0 <= psico_exam <= 100):
            raise ValueError("Input values are invalid!")

        # Creating an array with all input data and adjusting the shape
        input_data = np.array([english_test, iq_grade, psico_exam]).reshape(1, 3)

        # Dataframe com dados e nomes de colunas
        input_data_df = pd.DataFrame(input_data, columns=['nota_english_test', 'valor_qi', 'nota_psico_examtecnico'])

        # Standardizingh the new data
        input_data_standardized = scaler.transform(input_data_df)

        # Doing the prediction with the model using the standardized data
        pred = model.predict(input_data_standardized)
        
        result = 'The student can be enrolled' if pred[0] == 1 else 'The student cant be enrolled'

    except Exception as e:
        result = f"Error on prediction: {e}"

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run()
