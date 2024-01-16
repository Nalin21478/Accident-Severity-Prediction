from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Replace '/path/to/your/model.joblib' with the actual path to your saved model file
model = joblib.load('/Users/nalinarora/Desktop/Accident_severity_data/your_pipeline_filename.joblib')
@app.route('/', methods=['GET'])
def home():
    # Render the main page with photo and text
    return render_template('main.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get input values from the form
        distance = float(request.form['Distance(mi)'])
        temperature = float(request.form['Temperature(F)'])
        wind_chill = float(request.form['Wind_Chill(F)']) if request.form['Wind_Chill(F)'] else None
        humidity = float(request.form['Humidity(%)'])
        pressure = float(request.form['Pressure(in)'])
        visibility = float(request.form['Visibility(mi)'])
        wind_direction = request.form['Wind_Direction']
        wind_speed = float(request.form['Wind_Speed(mph)'])
        precipitation = float(request.form['Precipitation(in)'])
        weather_condition = request.form['Weather_Condition']
        crossing = request.form['Crossing'] == 'True'
        junction = request.form['Junction'] == 'True'
        traffic_signal = request.form['Traffic_Signal'] == 'True'
        sunrise_sunset = request.form['Sunrise_Sunset']
        day_type = request.form['Day_Type']
        season = request.form['Season']
        time_of_day = request.form['Time_Of_Day']
        duration = float(request.form['Duration'])

        # Create a DataFrame with the input data
        input_data = pd.DataFrame({
            'Distance(mi)': [distance],
            'Temperature(F)': [temperature],
            'Wind_Chill(F)': [wind_chill],
            'Humidity(%)': [humidity],
            'Pressure(in)': [pressure],
            'Visibility(mi)': [visibility],
            'Wind_Direction': [wind_direction],
            'Wind_Speed(mph)': [wind_speed],
            'Precipitation(in)': [precipitation],
            'Weather_Condition': [weather_condition],
            'Crossing': [crossing],
            'Junction': [junction],
            'Traffic_Signal': [traffic_signal],
            'Sunrise_Sunset': [sunrise_sunset],
            'Day_Type': [day_type],
            'Season': [season],
            'Time_Of_Day': [time_of_day],
            'Duration': [duration],
        })

        # Make a prediction using the loaded model
        prediction = model.predict(input_data)

        # Display the result on a new page
        return render_template('result.html', prediction=prediction[0])

    # Render the initial form on the home page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
