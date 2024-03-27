const accordionButtons = document.querySelectorAll(".accordion");

accordionButtons.forEach((button) => {
  button.addEventListener("click", function () {
    this.parentNode.classList.toggle("active");

    const panel = this.nextElementSibling;
    if (panel.style.display == "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
});
