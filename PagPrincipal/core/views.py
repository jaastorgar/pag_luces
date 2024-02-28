from django.shortcuts import render
from .models import Cliente, Producto, Reserva
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.db.models import Q 

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def arriendo(request):
    productos = Producto.objects.all()

    return render(request, 'core/Arriendo.html', {'productos': productos})

def iniciosesion(request):
    return render(request, 'core/inicioSesion.html')

def generar_informe_completo(request):
    # Obtén todos los objetos de los modelos relacionados
    clientes = Cliente.objects.prefetch_related('region', 'comuna').all()
    productos = Producto.objects.all()
    reservas = Reserva.objects.prefetch_related('cliente', 'producto').all()

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

    # Información de Reservas
    y -= 20
    pdf.drawString(100, y, "Información de Reservas:")
    for reserva in reservas:
        y -= 20
        pdf.drawString(100, y, f"Cliente: {reserva.carrito.cliente.nombreCliente}")
        y -= 15
        pdf.drawString(100, y, f"Producto: {reserva.producto.nombre}")
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
    reservas = Reserva.objects.all()

    # Renderizar la plantilla con los datos
    return render(request, 'informe_completo.html', {
        'clientes': clientes,
        'productos': productos,
        'reservas': reservas,
    })

def reservas(request):
    return render(request, 'core/reservaLuces.html')

def busquedas(request):
    query = request.GET.get('q')
    resultado = Producto.objects.filter(Q(nombre__icontains = query) | Q(descripcion = query))

    return render(request, 'core/Arriendo.html', {'resultado': resultado, 'query': query})