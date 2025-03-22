import pickle
import pandas as pd

# Load the model from the .pkl file
with open('rainfall_prediction_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Function to get user input
def get_user_input():
    print("Please enter the following details for rainfall prediction:")
    pressure = float(input("Pressure (hPa): "))
    dewpoint = float(input("Dewpoint (°C): "))
    humidity = int(input("Humidity (%): "))
    cloud = int(input("Cloud cover (%): "))
    sunshine = float(input("Sunshine (hours): "))
    winddirection = float(input("Wind Direction (degrees): "))
    windspeed = float(input("Wind Speed (km/h): "))

    # Return the input as a dictionary
    return {
        'pressure': [pressure],
        'dewpoint': [dewpoint],
        'humidity': [humidity],
        'cloud': [cloud],
        'sunshine': [sunshine],
        'winddirection': [winddirection],
        'windspeed': [windspeed]
    }

# Get user input
input_data = get_user_input()

# Convert the input data into a DataFrame
input_df = pd.DataFrame(input_data)

# Ensure the columns are in the correct order (same as during training)
input_df = input_df[['pressure', 'dewpoint', 'humidity', 'cloud', 'sunshine', 'winddirection', 'windspeed']]

# Now you can use loaded_model to make predictions
prediction = loaded_model.predict(input_df)
print("Prediction Result:", "Rainfall" if prediction[0] == 1 else "No Rainfall")