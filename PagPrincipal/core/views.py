from django.shortcuts import get_object_or_404, render, redirect
from .models import Cliente, Producto
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .forms import ClienteLoginForm, ClienteRegistroForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def arriendo(request):
    return render(request, 'core/Arriendo.html')

def generar_informe_completo(request):
    # Obtén todos los objetos de los modelos relacionados
    clientes = Cliente.objects.prefetch_related('region', 'comuna').all()
    productos = Producto.objects.all()

    # Configura el encabezado de la respuesta HTTP para indicar que es un archivo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="informe_completo.pdf"'

    # Crea el objeto PDF con reportlab
    pdf = canvas.Canvas(response)

    # Agrega contenido al PDF
    pdf.drawString(100, 800, "Informe Completo")

    # Información de Clientes
    y = 780
    pdf.drawString(100, y, "Información de Clientes:")
    for cliente in clientes:
        y -= 20
        pdf.drawString(100, y, f"Nombre: {cliente.nombreCliente}")
        y -= 15
        pdf.drawString(100, y, f"Teléfono: {cliente.telefono}")
        y -= 15
        pdf.drawString(100, y, f"Dirección: {cliente.direccion}")
        y -= 15
        pdf.drawString(100, y, f"Correo: {cliente.email}")
        
        # Manejo adecuado del campo ManyToManyField 'region'
        regiones = ', '.join(region.nombre for region in cliente.region.all()) if cliente.region.exists() else 'N/A'
        y -= 15
        pdf.drawString(100, y, f"Región: {regiones}")

        # Manejo adecuado del campo ManyToManyField 'comuna'
        comunas = ', '.join(comuna.nombre for comuna in cliente.comuna.all()) if cliente.comuna.exists() else 'N/A'
        y -= 15
        pdf.drawString(100, y, f"Comuna: {comunas}")
        
        y -= 20

    # Información de Productos
    y -= 20
    pdf.drawString(100, y, "Información de Productos:")
    for producto in productos:
        y -= 20
        pdf.drawString(100, y, f"Nombre: {producto.nombre}")
        y -= 15
        pdf.drawString(100, y, f"Descripción: {producto.descripcion}")
        y -= 15
        pdf.drawString(100, y, f"Precio: {producto.precio}")
        y -= 15
        pdf.drawString(100, y, f"Stock: {producto.stock}")
        y -= 20

    # Indica que la página está completa
    pdf.showPage()

    # Guarda el objeto PDF
    pdf.save()

    return response

def informe_completo(request):
    # Obtener datos de los modelos (ajusta según tus necesidades)
    clientes = Cliente.objects.all().prefetch_related('region', 'comuna')
    productos = Producto.objects.all()

    # Renderizar la plantilla con los datos
    return render(request, 'informe_completo.html', {
        'clientes': clientes,
        'productos': productos,
    })

def buscar_productos(request):
    try:
        query = request.GET.get('q', '')
        productos = Producto.objects.filter(nombre__icontains = query)
        return render(request, 'core/resultados_busqueda.html', {'productos': productos, 'query': query})
    except Exception as e:
        # Imprime o registra la excepción para depuración
        print(f"Error en la vista buscar_productos: {e}")
        return HttpResponse(status=500)
    
def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id = producto_id)

    return render(request, 'core/detalle_producto.html', {'producto': producto})

@csrf_protect
def cliente_login(request):
    if request.method == 'POST':
        form = ClienteLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            if user:
                login(request, user)

                return redirect('home')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = ClienteLoginForm()
    
    return render(request, 'core/cliente_login.html', {'form': form})

@csrf_protect
def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a la página de inicio de sesión o a donde desees después del registro
            return redirect('cliente_login')
    else:
        form = ClienteRegistroForm()

    return render(request, 'core/registro_cliente.html', {'form': form})