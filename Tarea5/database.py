#Interfaz de BaseData
from abc import ABC, abstractmethod

class  DataBase(ABC):
    @abstractmethod
    def insertar(self, data: str) -> bool: 
        self._data  = data
        return True
    
    @abstractmethod
    def eliminar(self, pos: int) -> bool:
        self._pos  = pos
        return True
    
    @abstractmethod
    def actualizar(self,data) -> None:
        self._data  = data
        return True

#Clase Reporte
class Reporte:
    def  __init__(self, id:int=None, baseDeDatos:DataBase = None):
        self._id = id
        self._baseDeDatos = baseDeDatos

    def abrir():
        pass