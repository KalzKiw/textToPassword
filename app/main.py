from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    if request.method == 'POST':
        text = request.form.get('text', '')
        # Tomar la primera letra de cada palabra, alternando mayúsculas/minúsculas
        letters = [word[0] for word in text.split() if word]
        # Alternar mayúsculas/minúsculas
        for i in range(len(letters)):
            letters[i] = letters[i].upper() if i % 2 == 0 else letters[i].lower()
        # Limitar a 12 caracteres
        password = ''.join(letters)[:12]
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
