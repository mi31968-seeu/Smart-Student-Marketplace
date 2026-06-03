const defaultUsers = [
  { name: "Demo Student", email: "student@example.com", password: "12345" }
];

const defaultServices = [
  {
    title: "Math Tutoring",
    category: "Tutoring",
    description: "Help with calculus, algebra, and exam preparation.",
    price: "10 EUR/hour",
    contact: "mustafa@student.com",
    owner: "Mustafa Ismaili",
    rating: 5
  },
  {
    title: "Programming Notes",
    category: "Notes",
    description: "Clean notes for Java, Python, and Software Engineering.",
    price: "5 EUR",
    contact: "amra@student.com",
    owner: "Amra Demiri",
    rating: 4
  },
  {
    title: "Laptop Stand Rental",
    category: "Renting",
    description: "Laptop stand available for short-term renting.",
    price: "2 EUR/day",
    contact: "student@example.com",
    owner: "Student User",
    rating: 4
  },
  {
    title: "English Assignment Help",
    category: "Other",
    description: "Help with formatting and proofreading academic assignments.",
    price: "8 EUR",
    contact: "support@student.com",
    owner: "Campus Helper",
    rating: 5
  }
];

const defaultReviews = [
  {
    name: "Student A",
    service: "Math Tutoring",
    text: "Very helpful tutoring session and clear explanations.",
    rating: 5
  },
  {
    name: "Student B",
    service: "Programming Notes",
    text: "The notes were organized and useful for exam preparation.",
    rating: 4
  },
  {
    name: "Student C",
    service: "Laptop Stand Rental",
    text: "Good communication and fair price.",
    rating: 4
  }
];

let users = JSON.parse(localStorage.getItem("studentMarketUsers")) || defaultUsers;
let services = JSON.parse(localStorage.getItem("studentMarketServices")) || defaultServices;
let currentUser = JSON.parse(localStorage.getItem("studentMarketCurrentUser")) || null;

function saveData() {
  localStorage.setItem("studentMarketUsers", JSON.stringify(users));
  localStorage.setItem("studentMarketServices", JSON.stringify(services));
  localStorage.setItem("studentMarketCurrentUser", JSON.stringify(currentUser));
}

function showToast(message) {
  const toast = document.getElementById("toast");
  toast.textContent = message;
  toast.classList.add("show");
  setTimeout(() => toast.classList.remove("show"), 2600);
}

function openAuth(mode) {
  document.getElementById("authModal").classList.add("show");
  document.getElementById("authMessage").textContent = "";

  if (mode === "register") {
    document.getElementById("loginForm").style.display = "none";
    document.getElementById("registerForm").style.display = "block";
  } else {
    document.getElementById("loginForm").style.display = "block";
    document.getElementById("registerForm").style.display = "none";
  }
}

function closeAuth() {
  document.getElementById("authModal").classList.remove("show");
}

function registerStudent() {
  const name = document.getElementById("registerName").value.trim();
  const email = document.getElementById("registerEmail").value.trim().toLowerCase();
  const password = document.getElementById("registerPassword").value;
  const message = document.getElementById("authMessage");

  if (!name || !email || !password) {
    message.textContent = "Please fill all registration fields.";
    message.className = "form-message error";
    return;
  }

  if (users.some(user => user.email === email)) {
    message.textContent = "This email is already registered.";
    message.className = "form-message error";
    return;
  }

  users.push({ name, email, password });
  currentUser = { name, email };
  saveData();
  updateUI();
  closeAuth();
  showToast("Account created successfully");
}

function loginStudent() {
  const email = document.getElementById("loginEmail").value.trim().toLowerCase();
  const password = document.getElementById("loginPassword").value;
  const message = document.getElementById("authMessage");

  const user = users.find(user => user.email === email && user.password === password);

  if (!user) {
    message.textContent = "Invalid email or password.";
    message.className = "form-message error";
    return;
  }

  currentUser = { name: user.name, email: user.email };
  saveData();
  updateUI();
  closeAuth();
  showToast("Login successful");
}

function logoutStudent() {
  currentUser = null;
  saveData();
  updateUI();
  showToast("Logged out");
}

function updateUI() {
  document.getElementById("userCount").textContent = users.length;
  document.getElementById("serviceCount").textContent = services.length;

  const currentUserText = document.getElementById("currentUserText");

  if (currentUser) {
    currentUserText.textContent = `Logged in as ${currentUser.name} (${currentUser.email})`;
  } else {
    currentUserText.textContent = "No student is currently logged in.";
  }

  renderServices();
  renderReviews();
}

function renderServices() {
  const list = document.getElementById("serviceList");
  const search = document.getElementById("searchInput").value.toLowerCase();
  const category = document.getElementById("categoryFilter").value;

  list.innerHTML = "";

  const filteredServices = services.filter(service => {
    const text = `${service.title} ${service.category} ${service.description} ${service.owner}`.toLowerCase();
    const matchesSearch = text.includes(search);
    const matchesCategory = category === "All" || service.category === category;
    return matchesSearch && matchesCategory;
  });

  if (filteredServices.length === 0) {
    list.innerHTML = "<p>No services found.</p>";
    return;
  }

  filteredServices.forEach(service => {
    const card = document.createElement("div");
    card.className = "service-card";
    card.innerHTML = `
      <div class="service-tag">${service.category}</div>
      <h3>${service.title}</h3>
      <p>${service.description}</p>
      <p><strong>Owner:</strong> ${service.owner}</p>
      <p><strong>Contact:</strong> ${service.contact}</p>
      <div class="service-meta">
        <span>${service.price}</span>
        <span class="rating">${"★".repeat(service.rating)}${"☆".repeat(5 - service.rating)}</span>
      </div>
    `;
    list.appendChild(card);
  });
}

function addService(event) {
  event.preventDefault();

  const message = document.getElementById("serviceMessage");

  if (!currentUser) {
    message.textContent = "Please login before adding a service.";
    message.className = "form-message error";
    return;
  }

  const title = document.getElementById("serviceTitle").value.trim();
  const category = document.getElementById("serviceCategory").value;
  const price = document.getElementById("servicePrice").value.trim();
  const contact = document.getElementById("serviceContact").value.trim();
  const description = document.getElementById("serviceDescription").value.trim();

  if (!title || !category || !price || !contact || !description) {
    message.textContent = "Please fill all fields.";
    message.className = "form-message error";
    return;
  }

  services.unshift({
    title,
    category,
    price,
    contact,
    description,
    owner: currentUser.name,
    rating: 5
  });

  saveData();
  updateUI();

  document.getElementById("serviceTitle").value = "";
  document.getElementById("serviceCategory").value = "";
  document.getElementById("servicePrice").value = "";
  document.getElementById("serviceContact").value = "";
  document.getElementById("serviceDescription").value = "";

  message.textContent = "Service added successfully.";
  message.className = "form-message success";
  showToast("New service added");
}

function renderReviews() {
  const reviewList = document.getElementById("reviewList");
  reviewList.innerHTML = "";

  defaultReviews.forEach(review => {
    const card = document.createElement("div");
    card.className = "review-card";
    card.innerHTML = `
      <div class="rating">${"★".repeat(review.rating)}${"☆".repeat(5 - review.rating)}</div>
      <h3>${review.service}</h3>
      <p>"${review.text}"</p>
      <p><strong>${review.name}</strong></p>
    `;
    reviewList.appendChild(card);
  });
}

updateUI();
