import requests
#importo requests q e sun archivo en el q hay preguntas y respuestas par aimprotarlas y pegarlas en el PY main
#En este caso hago estas peticiones d esta manera ps el archivo https esta subido a la nube y tiene respuestas y preguntas
parameters = {
    "amount": 10,
    "type": "multiple"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]

[
    {
        'category': 'Sports',
        'type': 'multiple',
        'difficulty': 'medium',
        'question': 'Manoloooooooooooo',
        'correct_answer': 'Alain Prost',
        'incorrect_answers': [
            'Ayrton Senna',
            'Niki Lauda',
            'Emerson Fittipaldi'
        ]
    },
    {
        'category': 'Entertainment: Music',
        'type': 'multiple',
        'difficulty': 'medium',
        'question': 'In which city did American rap producer DJ Khaled originate from?',
        'correct_answer': 'Miami',
        'incorrect_answers': [
            'New York',
            'Detroit',
            'Atlanta'
        ]
    }
]
