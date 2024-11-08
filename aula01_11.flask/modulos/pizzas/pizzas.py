from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Pizza

bp_pizza = Blueprint('pizzas', __name__, template_folder="templates")

@bp_pizza.route('/')
def index():
    dados = Pizza.query.all()
    return render_template('pizzas.html', pizzas = dados)

@bp_pizza.route('/add')
def add():
    return render_template('pizzas_add.html')

@bp_pizza.route('/save', methods=['POST'])
def save():
    sabor = request.form.get('sabor')
    ingredientes = request.form.get('ingredientes')
    preço = request.form.get('preço')
    if sabor and ingredientes and preço:
        bp_pizza = Pizza(sabor, ingredientes, preço)
        db.session.add(bd_pizza)
        db.session.commit()
        flash('Pizza salvo com sucesso!')
        return redirect('/')
    else:
        flash('Preencha todos os campos!')
        return redirect('/add')