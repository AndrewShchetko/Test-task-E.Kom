from django.http import JsonResponse
import json
from .validation import validate_form
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_forms_view(request) -> JsonResponse:
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        response = validate_form(data)
        return JsonResponse({'Response data': response})
    else:
        return JsonResponse({'ERROR': 'Only POST request is allowed'})
