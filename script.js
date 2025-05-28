document.getElementById('contact-form').addEventListener('submit', function (e) {
    e.preventDefault();
    alert("Thank you for contacting True Numbers. We'll respond shortly.");
    this.reset();
  });
  
document.addEventListener('DOMContentLoaded', function() {
  var collaborationsContent = document.querySelector('.collaborations-content');
  if (collaborationsContent) {
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          collaborationsContent.classList.add('visible');
          observer.disconnect();
        }
      });
    }, { threshold: 0.3 });
    observer.observe(collaborationsContent);
  }
});
  