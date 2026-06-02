const services = [
    {
        title: "Mathematics Tutoring",
        category: "Tutoring",
        description: "One-to-one tutoring for calculus, algebra, and exam preparation.",
        price: "500 MKD/hour",
        rating: "4.9"
    },
    {
        title: "Database Notes Package",
        category: "Notes",
        description: "Organized notes for database design, SQL queries, and normalization.",
        price: "300 MKD",
        rating: "4.8"
    },
    {
        title: "Laptop Rental for Presentations",
        category: "Rent",
        description: "Short-term laptop rental for presentations, labs, and group projects.",
        price: "700 MKD/day",
        rating: "4.7"
    },
    {
        title: "CV and Assignment Formatting",
        category: "Other",
        description: "Help with document formatting, project reports, and presentation design.",
        price: "400 MKD",
        rating: "4.6"
    },
    {
        title: "Programming Help",
        category: "Tutoring",
        description: "Support with Java, Python, web programming, and debugging tasks.",
        price: "600 MKD/hour",
        rating: "5.0"
    },
    {
        title: "Textbook Rental",
        category: "Rent",
        description: "Rent textbooks for software engineering and computer science subjects.",
        price: "250 MKD/week",
        rating: "4.5"
    }
];

const serviceList = document.getElementById("serviceList");
const emptyMessage = document.getElementById("emptyMessage");
const searchInput = document.getElementById("searchInput");
const serviceForm = document.getElementById("serviceForm");

function renderServices(items) {
    serviceList.innerHTML = "";

    if (items.length === 0) {
        emptyMessage.style.display = "block";
        return;
    }

    emptyMessage.style.display = "none";

    items.forEach((service) => {
        const card = document.createElement("article");
        card.className = "service-card";
        card.innerHTML = `
            <span class="category-pill">${service.category}</span>
            <h3>${service.title}</h3>
            <p>${service.description}</p>
            <div class="price-row">
                <strong>${service.price}</strong>
                <span class="rating">⭐ ${service.rating}</span>
            </div>
        `;
        serviceList.appendChild(card);
    });
}

function filterServices() {
    const keyword = searchInput.value.toLowerCase().trim();
    const filtered = services.filter((service) => {
        return (
            service.title.toLowerCase().includes(keyword) ||
            service.category.toLowerCase().includes(keyword) ||
            service.description.toLowerCase().includes(keyword)
        );
    });
    renderServices(filtered);
}

function setSearch(keyword) {
    searchInput.value = keyword;
    filterServices();
    document.getElementById("services").scrollIntoView({ behavior: "smooth" });
}

serviceForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const newService = {
        title: document.getElementById("title").value,
        category: document.getElementById("category").value,
        price: document.getElementById("price").value,
        description: document.getElementById("description").value,
        rating: "New"
    };

    services.unshift(newService);
    renderServices(services);
    serviceForm.reset();
    document.getElementById("services").scrollIntoView({ behavior: "smooth" });
});

searchInput.addEventListener("input", filterServices);

renderServices(services);
