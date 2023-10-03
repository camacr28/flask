from flask import redirect, render_template, request, url_for

from . import app
from .models import ListaMovimientos, Movimiento


@app.route('/')
def home():
    """
    Muestra la lista de movimientos cargados.
    """
    lista = ListaMovimientos()
    lista.leer_desde_archivo()

    return render_template(
        'inicio.html',
        movs=lista.movimientos)


@app.route('/nuevo', methods=['GET', 'POST'])
def add_movement():
    """
    Crea un movimiento nuevo y lo guarda en el archivo CSV

    1. Recibo una petición GET: pintar el formulario
    2. Recibo una petición POST:
        - Recojo los datos del formulario
        - Creo un objeto movimiento con esos datos
        - Validar que los datos son correctos, que el movimiento es válido
        - Utilizo la lista de movimientos para agregar el movimiento
        - Si todo es correcto, redireccionar a la lista de movimientos (home)
    """

    if request.method == 'GET':
        return render_template('nuevo.html')
    if request.method == 'POST':
        mov = Movimiento(request.form)
        if mov.has_errors:
            return f'Error: el movimiento no es válido. {mov.errores}'
        lista = ListaMovimientos()
        lista.leer_desde_archivo()
        lista.agregar(mov)
        return redirect(url_for('home'))


@app.route('/modificar')
def update():
    """
    Permite editar los datos de un movimiento creado previamente.
    """
    return 'Actualizar movimiento'


@app.route('/borrar')
def delete():
    """
    Borra un movimiento existente.
    """
    return 'Borrar movimiento'
