import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        """Funzione per la ricerca delle parole errate, in accordo con le modalità specificate"""
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = ""

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        """Funzione per la stampa di un menù"""
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def handleLanguage(self, e):
        """Funzione per la verifica di inserimento di una lingua corretta"""
        if self._view._langList.value is not None:
            self._view._control.value=f"Hai inserito correttamente la lingua {self._view._langList.value}"
            self._view.page.update()

    def handleModality(self, e):
        """Funzione per la verifica di inserimento di una modalità corretta"""
        if self._view._modality.value is not None:
            self._view._control1.value=f"Hai inserito correttamente la modalità {self._view._modality.value}"
            self._view.page.update()

    def handleSpellCheck(self, e):
         """Funzione per la gestione del risultato e di verifica di corretti valori in tutti i campi"""
         if (self._view._langList.value is None) or (self._view._modality.value is None) or (self._view.txtIn.value==""):
              self._view.txtOut3.value=("Errore. Compilare tutti i campi.")
              self._view.page.add(self._view.txtOut3)
              return
         paroleErrate, time=self.handleSentence(self._view.txtIn.value,self._view._langList.value,self._view._modality.value)
         self.handleRisultato(paroleErrate,time)
         self._view.txtIn.value = ""
         self._view.txtIn.update()


    def handleRisultato(self, paroleErrate, time):
        """Funzione per la stampa del risultato"""
        self._view._frase.value=f"Frase inserita: {self._view.txtIn.value}"
        self._view._parole.value = f"Parole errate - {self._multiDic.printWordErrate(paroleErrate)}"
        self._view._tempo.value = f"Tempo richiesto dalla ricerca {time}"
        self._view.page.add(self._view._risultato)


def replaceChars(text):
        """Funzione per la rimozione di caratteri speciali"""
        chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
        for c in chars:
            text = text.replace(c, "")
        return text