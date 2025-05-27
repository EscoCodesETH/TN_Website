document.getElementById('contact-form').addEventListener('submit', function (e) {
    e.preventDefault();
    alert("Thank you for contacting True Numbers. We'll respond shortly.");
    this.reset();
  });
  