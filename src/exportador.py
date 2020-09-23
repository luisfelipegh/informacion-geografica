from abc import ABC, abstractmethod
import Nodo

class IExportador(ABC):

    def __init__(self, arg):
        pass

    @abstractmethod
    def exportar(self, msj):
        pass

class ExportadorXML(IExportador):

    def __init__(self):
        super().__init__()

    def exportar(self):
        print('Exportado como XML')


class ExportadorPDF(IExportador):

    def __init__(self):
        super().__init__()

    def exportar(self):
        print('Exportado como PDF')
