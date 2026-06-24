#Bibliotecas usadas
import argostranslate.package
from PySide6.QtGui import QIcon
import argostranslate.translate
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
import os
import sys

def caminho_recurso(nome):
        if getattr(sys, "frozen", False):
                return os.path.join(sys._MEIPASS, nome)
        return os.path.join(os.path.dirname(__file__), nome)

def tradutor(texto_usuario,idioma_origem,idioma_destino):
        try:
                from_code = idioma_origem
                to_code = idioma_destino

                # Download e instalação do pacote Argos Translate
                argostranslate.package.update_package_index()
                available_packages = argostranslate.package.get_available_packages()
                package_to_install = next(
                filter(
                        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
                )
                )
                argostranslate.package.install_from_path(package_to_install.download())

                # tradução
                texto_traduzido = argostranslate.translate.translate(texto_usuario, from_code, to_code)

                return texto_traduzido

        except Exception:
                return 'Erro: Não foi possível realizar a tradução.'
class Tradutor:
        def __init__(self):
        #Carregador do arquivo da GUI
                carregador=QUiLoader()
                self.ui=carregador.load(caminho_recurso('desing_tradutor.ui'))

                #Titulo do software e seu icone
                self.ui.setWindowTitle('Tradutor')
                self.ui.setWindowIcon(QIcon(caminho_recurso('logo_tradutor.ico')))

                #Botão para traduzir o texto
                self.ui.botao_traduzir.clicked.connect(self.traduzir)

                # Idiomas já selecionados por padrão

                self.ui.botao_portugues_tt.setChecked(True)
                self.ui.botao_ingles_it.setChecked(True)

        def botao_texto_original(self):
                if self.ui.botao_portugues_it.isChecked():
                        return 'pt'
                elif self.ui.botao_ingles_it.isChecked():
                        return 'en'
                elif self.ui.botao_espanhol_it.isChecked():
                        return 'es'


        def botao_texto_traducao(self):
                if self.ui.botao_portugues_tt.isChecked():
                        return 'pt'
                elif self.ui.botao_ingles_tt.isChecked():
                        return 'en'
                elif self.ui.botao_espanhol_tt.isChecked():
                        return 'es'

        def traduzir(self):
                #Coleto do texto do usuario e tradução
                self.texto_usuario=str(self.ui.caixa_texto.text())

                idioma_origem = self.botao_texto_original()
                idioma_destino = self.botao_texto_traducao()

                var_temp_txt=tradutor(self.texto_usuario,idioma_origem,idioma_destino)

                #devolutiva da texto transcrito
                campo_texto_traduzido=self.ui.caixa_texto_2
                campo_texto_traduzido.setText(var_temp_txt)

                #A linha abaixo coloca o texto transcrito somente para modo leitura
                campo_texto_traduzido.setReadOnly(True)

if __name__ == '__main__':
        app = QApplication()
        interfaces = Tradutor()
        interfaces.ui.show()
        app.exec()