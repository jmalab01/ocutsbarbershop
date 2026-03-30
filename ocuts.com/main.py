from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the about page
@app.route('/team')
def about():
    return render_template('about.html')

# Route for the services page
@app.route('/services')
def services():
    return render_template('services.html')

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route to handle booking form submission
@app.route('/book', methods=['POST'])
def book():
    date = request.form['date']
    service = request.form['service']
    time = request.form['time']
    phone = request.form.get('phone', 'N/A')
    email = request.form.get('email', 'N/A')

    # Save the booking to the database
    conn = sqlite3.connect('appointments.db')
    c = conn.cursor()
    c.execute("INSERT INTO appointments (date, service, time, phone, email) VALUES (?, ?, ?, ?, ?)",
              (date, service, time, phone, email))
    conn.commit()
    conn.close()

    # Redirect to a thank you or confirmation page
    return redirect(url_for('thank_you'))

# Route for the thank you page
@app.route('/thank-you')
def thank_you():
    return "Thank you for your booking!"

# Route to provide available dates (for example purposes)
@app.route('/available-dates')
def available_dates():
    return jsonify(availableDates=["2024-09-01", "2024-09-02"], unavailableDates=["2024-09-03"])

# Route to provide available times for a specific date
@app.route('/available-times')
def available_times():
    date = request.args.get('date')
    # Example logic for available times
    return jsonify(bookedTimes=["12:00 PM", "1:00 PM"])

if __name__ == '__main__':
    app.run(debug=True)
