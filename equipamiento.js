document.addEventListener("DOMContentLoaded", function() {
    const content = document.getElementById("content");
  
    fetchCategories("./equipamiento/")
      .then(data => {
        data.forEach(category => {
          const categoryDiv = document.createElement("div");
          categoryDiv.classList.add("category");
          const categoryTitle = document.createElement("h2");
          categoryTitle.textContent = category.name;
          categoryDiv.appendChild(categoryTitle);
          
          const container = document.createElement("div");
          container.classList.add("container");
  
          category.items.forEach(item => {
            try {
              const card = document.createElement("div");
              card.classList.add("card");
  
              // Construir la ruta de la imagen automáticamente
              const imgPath = `./equipamiento/${item.image}.png`;
  
              const imgTag = document.createElement("img");
              imgTag.src = imgPath;
              card.appendChild(imgTag);
              
              const title = document.createElement("div");
              title.classList.add("card-title");
              title.textContent = item.title;
              card.appendChild(title);
              
              const description = document.createElement("div");
              description.classList.add("card-description");
              description.textContent = item.description;
              card.appendChild(description);
  
              const price = document.createElement("div");
              price.classList.add("card-price");
              price.textContent = `Precio: ${item.price}`;
              card.appendChild(price);
  
              // Evento para abrir el modal con más detalles
              card.addEventListener("click", () => openModal(item));
  
              container.appendChild(card);
            } catch (error) {
              console.error(`Error procesando el archivo para el item: ${item.title}`, error);
            }
          });
  
          categoryDiv.appendChild(container);
          content.appendChild(categoryDiv);
        });
      })
      .catch(err => console.error("Error cargando los archivos:", err));
  });
  
  async function fetchCategories(path) {
    const categories = [];
    
    const categoriesData = [
      {
        name: "Armas",
        items: await fetchJsonFile(path + "Armas.json")
      }
    ];
  
    return categoriesData;
  }
  
  async function fetchJsonFile(filePath) {
    const items = [];
  
    try {
      const response = await fetch(filePath);
  
      if (!response.ok) {
        throw new Error(`Error al obtener el archivo JSON: ${response.statusText}`);
      }
  
      const jsonData = await response.json();
  
      // Procesamos cada artículo del JSON
      for (const item of jsonData) {
        items.push(item);
      }
    } catch (err) {
      console.error("Error al procesar el archivo JSON:", err);
    }
  
    return items;
  }
  
  // Función para abrir el modal con toda la información
  function openModal(item) {
    const overlay = document.createElement("div");
    overlay.classList.add("overlay");
  
    const modalContent = document.createElement("div");
    modalContent.classList.add("modal-content");
  
    const imgPath = `./equipamiento/${item.image}.png`;
  
    modalContent.innerHTML = `
      <div class="modal-header">
        <img src="${imgPath}" alt="${item.title}" class="modal-image">
        <h3>${item.title}</h3>
        <button class="close-btn">&times;</button>
      </div>
      <div class="modal-body">
        <p><strong>Origen:</strong> ${item.origin}</p>
        <p><strong>Tipo de objeto:</strong> ${item.type}</p>
        <p><strong>Categoría:</strong> ${item.category}</p>
        <p><strong>Alcance:</strong> ${item.range}</p>
        <p><strong>Tipo de daño:</strong> ${item.damageType}</p>
        <p><strong>Para golpear:</strong> ${item.critical}</p>
        <p><strong>Daño:</strong> ${item.damage}</p>
        <p><strong>Precio:</strong> ${item.price}</p>
        <p><strong>Peso:</strong> ${item.weight}</p>
        <p><strong>Encantamientos:</strong> ${item.enchantments}</p>
        <ul>
          <li><strong>Propiedades:</strong></li>
          ${item.properties.map(prop => `<li>${prop}</li>`).join('')}
        </ul>
      </div>
    `;
  
    // Cerrar el modal
    const closeButton = modalContent.querySelector(".close-btn");
    closeButton.addEventListener("click", () => overlay.remove());
  
    overlay.appendChild(modalContent);
    document.body.appendChild(overlay);
  }
  