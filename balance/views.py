from flask import render_template
from . import app


@app.route('/')
def home():
    """
    Mostrar lista de movimientos cargados.
    """

    return render_template('inicio.html')


@app.route('/nuevo')
def add_movement():
    """
    Crear movimiento nuevo y guardarlo en archivo .csv.
    """
    return 'Agregar nuevo movimiento.'


@app.route('/modificar')
def update():
    """
    Editar datos de un movimiento creado previamente.
    """
    return 'Actualizar movimiento.'


@app.route('/borrar')
def delete():
    """
    Borra un movimiento existente.
    """
    return 'Borrar movimiento.'
