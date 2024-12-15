from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

def chat_home(request):
    return render(request, 'turismoai_app/chat.html')

@csrf_exempt
def chat_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            
            # Enviar mensaje al servidor de Rasa
            rasa_response = requests.post(
                'http://localhost:5005/webhooks/rest/webhook',
                json={"sender": "user", "message": user_message}
            )
            
            # Procesar respuesta de Rasa
            bot_responses = rasa_response.json()
            if bot_responses:
                # Concatenar todos los mensajes de la respuesta
                bot_message = '<br><br>'.join(
                    response['text'] for response in bot_responses
                )
                
                # Asegurarse de que los saltos de línea se preserven
                bot_message = bot_message.replace('\n', '<br>')
                bot_message = bot_message.replace('\r', '')
                
                print("Final message:", bot_message)  # Debug
            else:
                bot_message = "Lo siento, no pude procesar tu mensaje."
            
            return JsonResponse({
                'bot_message': bot_message,
                'full_response': bot_responses
            })
            
        except Exception as e:
            print(f"Error in chat_message: {str(e)}")
            return JsonResponse({
                'error': str(e),
                'details': f"Full error: {repr(e)}"
            }, status=500)
    return JsonResponse({'error': 'Método no permitido'}, status=405)
