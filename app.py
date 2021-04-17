from flask import Flask, render_template
from datetime import date


app = Flask(__name__)


def idade(dia, mes, ano):
	hoje = date.today()
	if hoje.month == mes:
		if hoje.day > dia:
			return hoje.year - ano
		else:
			return hoje.year - ano - 1
	elif hoje.month > mes:
		return hoje.year - ano
	else:
		return hoje.year - ano - 1



@app.route('/')
def index():
	idade_familia = []
	idade_familia.append(idade(21, 12, 1990))
	idade_familia.append(idade(23, 2, 2012))
	idade_familia.append(idade(9, 3, 2016))
	idade_familia.append(idade(28, 11, 1989))
	print(idade_familia)
	return render_template('index.html', idade=idade_familia)


if __name__ == '__main__':
    app.run()
