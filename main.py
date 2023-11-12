from flask import Flask, render_template, request
import random
import logging 

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='main.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def index():
    n = random.randrange(1, 10)
    app.logger.info(f"New game started. Target number: {n}")
    return render_template('index.html', target_number=n)

@app.route('/check_guess', methods=['POST'])
def check_guess():
    guess = int(request.form['guess'])
    target_number = int(request.form['target_number'])

    if guess < target_number:
        message = f'It is Higher than {guess}'
        app.logger.info(f"User guessed {guess}. It's higher than the target.")
    elif guess > target_number:
        message = f'It is Less than {guess}'
        app.logger.info(f"User guessed {guess}. It's less than the target.")
    else:
        message = f'Eureka!!! You nailed it. It\'s {guess}'
        app.logger.info(f"User guessed the correct number: {guess}")

    return render_template('index.html', message=message, target_number=target_number)

if __name__ == '__main__':
    app.run(debug=True)

