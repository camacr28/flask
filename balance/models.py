import csv
from datetime import date
from . import RUTA_FICHERO


class Movimiento:
    def __init__(self, fecha, concepto, tipo, cantidad):
        try:
            self.fecha = date.fromisoformat(fecha)
        except ValueError:
            self.fecha = None
            print(f'La fecha {fecha} no es válida.')
        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad

    def __str__(self):
        return f'{self.fecha} | {self.concepto} | {self.tipo} | {self.cantidad}'


class ListaMovimientos:
    def __init__(self):
        self.lista_movimientos = []

    def leer_desde_archivo(self):
        self.lista_movimientos = []
        with open(RUTA_FICHERO, 'r', encoding='UTF-8') as fichero:
            reader = csv.DictReader(fichero)
            for fila in reader:
                movimiento = Movimiento(
                    fila['fecha'],
                    fila['concepto'],
                    fila['ingreso_gasto'],
                    fila['cantidad'])
                self.lista_movimientos.append(fila)

    def __str__(self):
        result = ''
        for mov in self.lista_movimientos:
            result += f'\n{mov}'
        return result
