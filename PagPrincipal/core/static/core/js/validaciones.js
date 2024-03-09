// Configura el intervalo de cambio de imágenes (en milisegundos)
const intervalo = 3000; // Cambia la imagen cada 3 segundos

// Obtiene todas las tarjetas del carrusel
const tarjetas = document.querySelectorAll('.tarjetaCarrusel');

// Inicializa el índice de la imagen actual
let indiceActual = 0;

// Función para cambiar la imagen
function cambiarImagen() {
  // Oculta todas las tarjetas
  tarjetas.forEach(tarjeta => {
    tarjeta.style.display = 'none';
  });

  // Muestra la siguiente tarjeta
  tarjetas[indiceActual].style.display = 'block';

  // Incrementa el índice
  indiceActual = (indiceActual + 1) % tarjetas.length;
}

// Inicia el cambio de imágenes
const carruselInterval = setInterval(cambiarImagen, intervalo);

// Detiene el carrusel al colocar el mouse sobre él
document.getElementById('conteItemsCarrusel').addEventListener('mouseenter', () => {
  clearInterval(carruselInterval);
});

// Reanuda el carrusel al quitar el mouse
document.getElementById('conteItemsCarrusel').addEventListener('mouseleave', () => {
  carruselInterval = setInterval(cambiarImagen, intervalo);
});