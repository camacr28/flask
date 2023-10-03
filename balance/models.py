import csv
from datetime import date

from . import RUTA_FICHERO

CLAVES_IGNORADAS = ['errores']


class Movimiento:
    def __init__(self, dic_datos):
        # TODO: no puede tener fecha futura

        self.errores = []
        fecha = dic_datos.get('fecha', '')
        concepto = dic_datos.get('concepto', 'Gastos varios')
        tipo = dic_datos.get('tipo')
        cantidad = dic_datos.get('cantidad')

        try:
            self.fecha = date.fromisoformat(fecha)
        except ValueError:
            self.fecha = None
            self.errores.append(f'La fecha {fecha} no es una fecha válida')
        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad

    @property
    def has_errors(self):
        return len(self.errores) > 0

    def __str__(self):
        return f'{self.fecha}\t{self.concepto}\t{self.tipo}\t{self.cantidad}\n'

    def __repr__(self):
        return self.__str__()


class ListaMovimientos:
    def __init__(self):
        self.movimientos = []

    def leer_desde_archivo(self):
        self.movimientos = []
        with open(RUTA_FICHERO, 'r') as fichero:
            reader = csv.DictReader(fichero)
            for fila in reader:
                movimiento = Movimiento(fila)
                self.movimientos.append(movimiento)

    def agregar(self, movimiento):
        """
        Agrega el movimiento a la lista y actualiza el CSV
        """
        if not isinstance(movimiento, Movimiento):
            raise ValueError('No puedes agregar eso, no es un movimiento')
        self.movimientos.append(movimiento)
        self.guardar_archivo()

    def guardar_archivo(self):
        """
        Actualiza el archivo CSV con los movimientos que
        hay en la lista de movimientos.

        1. Vaciar el archivo
        2. Escribir la cabecera del fichero con los nombres de los campos
        3. Conocer la ruta del fichero donde lo tenemos que guardar
        4. Recoger (de la lista) cada dato y guardarlo en una línea (en el archivo) separada por comas
        5. (Opcional) Podemos ordenarlos por fecha
        """

        with open(RUTA_FICHERO, 'w') as csvfile:
            # cabeceras = ['fecha', 'concepto', 'tipo', 'cantidad']
            # writer = csv.writer(csvfile)
            # writer.writerow(cabeceras)

            cabeceras = list(self.movimientos[0].__dict__.keys())
            for clave in CLAVES_IGNORADAS:
                cabeceras.remove(clave)

            writer = csv.DictWriter(csvfile, fieldnames=cabeceras)
            writer.writeheader()

            for mov in self.movimientos:
                mov_dict = mov.__dict__
                for clave in CLAVES_IGNORADAS:
                    mov_dict.pop(clave)
                writer.writerow(mov_dict)

    def __str__(self):
        result = ''
        for mov in self.movimientos:
            result += f'\n{mov}'
        return result

    def __repr__(self):
        return self.__str__()
