# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# URL base de la API de Django
API_BASE_URL = "http://localhost:8000/api/"

class ActionConsultarRestaurantes(Action):
    def name(self) -> Text:
        return "action_consultar_restaurantes"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            response = requests.get(f"{API_BASE_URL}restaurantes/")
            restaurantes = response.json()
            
            if restaurantes:
                message = "🍽️ Estos son algunos restaurantes en Mérida:\n\n"
                for rest in restaurantes:
                    message += (f"🏠 {rest['nombre']}\n"
                              f"🍳 Tipo: {rest['tipo_cocina']}\n"
                              f"📍 {rest['direccion']}\n"
                              f"⏰ {rest['horario']}\n\n")
            else:
                message = "Lo siento, no encontré restaurantes en la base de datos."
                
            dispatcher.utter_message(text=message)
        except Exception as e:
            dispatcher.utter_message(text="Lo siento, hubo un error al consultar la API.")
        return []

class ActionConsultarAtracciones(Action):
    def name(self) -> Text:
        return "action_consultar_atracciones"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            response = requests.get(f"{API_BASE_URL}atracciones/")
            atracciones = response.json()
            
            if atracciones:
                message = "🏛️ Estas son algunas atracciones turísticas en Mérida:\n\n"
                for atrac in atracciones:
                    message += (f"🏺 {atrac['nombre']}\n"
                              f"📝 {atrac['descripcion']}\n"
                              f"⏰ {atrac['horario']}\n"
                              f"💰 ${atrac['precio']}\n\n")
            else:
                message = "Lo siento, no encontré atracciones turísticas en la base de datos."
                
            dispatcher.utter_message(text=message)
        except Exception as e:
            dispatcher.utter_message(text="Lo siento, hubo un error al consultar la API.")
        return []

class ActionConsultarActividades(Action):
    def name(self) -> Text:
        return "action_consultar_actividades"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            response = requests.get(f"{API_BASE_URL}actividades/")
            actividades = response.json()
            
            if actividades:
                message = "🌳 Estas son algunas actividades al aire libre en Mérida:\n\n"
                for act in actividades:
                    message += (f"🎯 {act['nombre']}\n"
                              f"📝 {act['descripcion']}\n"
                              f"⏰ {act['horario']}\n"
                              f"📊 Nivel: {act['nivel_dificultad']}\n"
                              f"🎒 Equipo: {act['equipo_necesario']}\n\n")
            else:
                message = "Lo siento, no encontré actividades al aire libre en la base de datos."
                
            dispatcher.utter_message(text=message)
        except Exception as e:
            dispatcher.utter_message(text="Lo siento, hubo un error al consultar la API.")
        return []

class ActionConsultarCultura(Action):
    def name(self) -> Text:
        return "action_consultar_cultura"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            response = requests.get(f"{API_BASE_URL}cultura/")
            cultura = response.json()
            
            if cultura:
                message = "🎭 Estos son algunos lugares culturales en Mérida:\n\n"
                for cult in cultura:
                    message += (f"🎪 {cult['nombre']}\n"
                              f"🏛️ Tipo: {cult['tipo']}\n"
                              f"📝 {cult['descripcion']}\n"
                              f"⏰ {cult['horario']}\n"
                              f"💰 ${cult['precio']}\n\n")
            else:
                message = "Lo siento, no encontré lugares culturales en la base de datos."
                
            dispatcher.utter_message(text=message)
        except Exception as e:
            dispatcher.utter_message(text="Lo siento, hubo un error al consultar la API.")
        return []

class ActionConsultarCompras(Action):
    def name(self) -> Text:
        return "action_consultar_compras"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            response = requests.get(f"{API_BASE_URL}compras/")
            compras = response.json()
            
            if compras:
                message = "🛍️ Estos son algunos lugares para compras en Mérida:\n\n"
                for comp in compras:
                    message += (f"🏪 {comp['nombre']}\n"
                              f"📍 {comp['direccion']}\n"
                              f"⏰ {comp['horario']}\n"
                              f"🛒 Productos: {comp['productos']}\n\n")
            else:
                message = "Lo siento, no encontré lugares para compras en la base de datos."
                
            dispatcher.utter_message(text=message)
        except Exception as e:
            dispatcher.utter_message(text="Lo siento, hubo un error al consultar la API.")
        return []

class ActionConsultarVidaNocturna(Action):
    def name(self) -> Text:
        return "action_consultar_vida_nocturna"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            response = requests.get(f"{API_BASE_URL}vidanocturna/")
            lugares = response.json()
            
            if lugares:
                message = "🌙 Estos son algunos lugares para salir de noche en Mérida:\n\n"
                for lugar in lugares:
                    message += (f"🎉 {lugar['nombre']}\n"
                              f"🎵 Tipo: {lugar['tipo']}\n"
                              f"📍 {lugar['direccion']}\n"
                              f"⏰ {lugar['horario']}\n"
                              f"💰 Entrada: ${lugar['precio_entrada']}\n\n")
            else:
                message = "Lo siento, no encontré lugares de vida nocturna en la base de datos."
                
            dispatcher.utter_message(text=message)
        except Exception as e:
            dispatcher.utter_message(text="Lo siento, hubo un error al consultar la API.")
        return []