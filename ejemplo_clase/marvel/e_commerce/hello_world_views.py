# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# NOTE: Ejemplo de hello world con método GET
def hello_world_view(request):
    template = f'<h1>Method not allowed: {request.method}</h1>'
    if request.method == 'GET':
        template = '<h1>Hello world Django APIs!</h1>' 
    return HttpResponse(template)


# NOTE: Ejemplo de hello world con método GET y POST
@csrf_exempt
def request_data_view(request):
    '''
    Esta función nos permite realizar una petición de tipo POST.
    Retorna el valor del parámetro "mi_parametro" enviada en la petición.
    '''
    template = f'<h1>Method not Allowed: {request.method}</h1>'
    if request.method == 'GET':
        template = f'<h1>{request.GET.get("mi_parametro")}</h1>'
    elif request.method == 'POST':
        # Tambien podemos llamar al método dentro de request, haciendo:
        data = request.POST.get('username')
        template = f'<h1>{data}</h1>'
    print(template)
    return HttpResponse(template)
