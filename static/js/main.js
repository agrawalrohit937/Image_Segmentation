// document.addEventListener("DOMContentLoaded", function () {
//   const dropArea = document.getElementById("drop-area");
//   const fileInput = document.getElementById("fileElem");

//   dropArea.addEventListener("click", () => fileInput.click());

//   dropArea.addEventListener("dragover", (e) => {
//     e.preventDefault();
//     dropArea.classList.add("dragging");
//   });

//   dropArea.addEventListener("dragleave", () => {
//     dropArea.classList.remove("dragging");
//   });

//   dropArea.addEventListener("drop", (e) => {
//     e.preventDefault();
//     dropArea.classList.remove("dragging");
//     fileInput.files = e.dataTransfer.files;
//   });
// });


document.addEventListener("DOMContentLoaded", () => {
  // === Theme Toggle ===
  const toggle = document.getElementById("theme-toggle");
  const html = document.documentElement;

  const savedTheme = localStorage.getItem("theme") || "light";
  html.setAttribute("data-theme", savedTheme);

  toggle.addEventListener("click", () => {
    const newTheme = html.getAttribute("data-theme") === "light" ? "dark" : "light";
    html.setAttribute("data-theme", newTheme);
    localStorage.setItem("theme", newTheme);
  });

  // === Drag & Drop Upload ===
  const dropArea = document.getElementById("drop-area");
  const fileInput = document.getElementById("fileElem");
  const previewContainer = document.getElementById("preview-container");

  if (dropArea && fileInput) {
    dropArea.addEventListener("click", () => fileInput.click());

    dropArea.addEventListener("dragover", (e) => {
      e.preventDefault();
      dropArea.classList.add("dragging");
    });

    dropArea.addEventListener("dragleave", () => {
      dropArea.classList.remove("dragging");
    });

    dropArea.addEventListener("drop", (e) => {
      e.preventDefault();
      dropArea.classList.remove("dragging");
      fileInput.files = e.dataTransfer.files;

      showPreview(fileInput.files[0]);
    });

    fileInput.addEventListener("change", () => {
      if (fileInput.files.length > 0) {
        showPreview(fileInput.files[0]);
      }
    });
  }

  function showPreview(file) {
    if (!file.type.startsWith("image/")) return;

    const reader = new FileReader();
    reader.onload = function (e) {
      previewContainer.innerHTML = "";
      const img = document.createElement("img");
      img.src = e.target.result;
      img.alt = "Image Preview";
      img.style.maxWidth = "300px";
      img.style.borderRadius = "10px";
      img.style.marginTop = "10px";
      previewContainer.appendChild(img);
    };
    reader.readAsDataURL(file);
  }

  // === Show loader on form submit ===
  const form = document.querySelector("form");
  const loader = document.getElementById("loader");

  if (form && loader) {
    form.addEventListener("submit", () => {
      loader.style.display = "block";
    });
  }
});
