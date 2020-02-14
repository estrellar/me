from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Resume(Resource):
    def get(self):
        return {
            'self': {
                'name': 'Rodrigo Estrella',
                'linkedIn': 'https://www.linkedin.com/in/rodrigo-estrella-0a6425b1'
            },
            'projects': [
                {
                    'name': 'This',
                    'description': 'This website',
                    'link': '#'
                },
                {
                    'name': 'Terminator',
                    'description': 'Electron app to install terminal themes',
                    'link': 'https://github.com/estrellar/macos-terminal-themes'
                }
            ],
            'jobs': [
                {
                    'employer': 'XiO Inc.',
                    'start_date': '2018-08',
                    'end_date': None,
                    'position': 'Software Engineer',
                    'responsibilites': [

                    ]
                },
                {
                    'employer': 'Sonoma County Information Systems Department',
                    'postition': 'Intern',
                    'start_date': '2016-07',
                    'end_date': '2018-08',
                    'responsibilities': [

                    ]
                }
            ],
            'education': [

            ]
        }


api.add_resource(Resume, '/')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
