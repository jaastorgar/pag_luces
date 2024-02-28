from django.shortcuts import render
from .models import Cliente, Producto, Reserva
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.db.models import Q 
from .filters import ReservaFilter
from django_filters.views import FilterView


# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def arriendo(request):
    return render(request, 'core/Arriendo.html')

def iniciosesion(request):
    return render(request, 'core/inicioSesion.html')

def generar_informe_completo(request):
    # Obtén todos los objetos de los modelos relacionados
    clientes = Cliente.objects.prefetch_related('region', 'comuna').all()
    productos = Producto.objects.all()
    reservas = Reserva.objects.prefetch_related('carrito__cliente', 'producto').all()

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
        pdf.drawString(100, y, f"Carrito del Cliente: {reserva.carrito.id}")
        y -= 15
        pdf.drawString(100, y, f"Producto: {reserva.producto.nombre}")
        y -= 20
        pdf.drawString(100, y, f"Cantidad: {reserva.cantidad}")
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

class ListaReservasView(FilterView):
    model = Reserva
    template_name = 'reserva_filter.html'
    filterset_class = ReservaFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset