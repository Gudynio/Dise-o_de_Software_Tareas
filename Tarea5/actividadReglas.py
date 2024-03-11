from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime

from pruebadatabasemysql import *


# Implementacion MySQL
dbMySQL = MySQL("sql10.freesqldatabase.com","sql10689405","ACM1wVFXPb","sql10689405")
reporte1 = Reporte(1,dbMySQL)

reporte1._baseDeDatos.insertar("Reporte","testIOnsert","2024-03-15")
reporte1._baseDeDatos.abrir("2024-03-15")
reporte1._baseDeDatos.actualizar("Reporte","Hola","2024-03-15")
reporte1._baseDeDatos.eliminar("Reporte","2024-03-15")
reporte1._baseDeDatos.abrir("2024-03-15")
'''
print(dbMySQL.insertar("Reporte","Informacion que cura","2024-03-07"))
dbMySQL.imprimir_registros("Reporte")
print(dbMySQL.actualizar("Reporte","Informacion que no cura","2024-03-07"))
dbMySQL.imprimir_registros("Reporte")
print(dbMySQL.eliminar("Reporte","2024-03-07"))
dbMySQL.imprimir_registros("Reporte")
'''