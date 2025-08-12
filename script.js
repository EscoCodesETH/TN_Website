// ===========================
// DOM Elements
// ===========================
const contactForm = document.getElementById('contact-form');
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');
const header = document.querySelector('header');
const collaborationsContent = document.querySelector('.collaborations-content');

// ===========================
// Contact Form Handler
// ===========================
if (contactForm) {
  contactForm.addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Get form data
    const formData = new FormData(this);
    const data = Object.fromEntries(formData);
    
    // Show success message
    const button = this.querySelector('button[type="submit"]');
    const originalText = button.textContent;
    button.textContent = 'Message Sent!';
    button.disabled = true;
    
    // Reset form
    this.reset();
    
    // Reset button after delay
    setTimeout(() => {
      button.textContent = originalText;
      button.disabled = false;
    }, 3000);
    
    // Log form data (replace with actual backend integration)
    console.log('Form submitted:', data);
  });
}

// ===========================
// Mobile Navigation Toggle
// ===========================
if (navToggle) {
  navToggle.addEventListener('click', function() {
    navLinks.classList.toggle('active');
    this.classList.toggle('active');
    
    // Animate hamburger menu
    const spans = this.querySelectorAll('span');
    if (this.classList.contains('active')) {
      spans[0].style.transform = 'rotate(45deg) translateY(8px)';
      spans[1].style.opacity = '0';
      spans[2].style.transform = 'rotate(-45deg) translateY(-8px)';
    } else {
      spans[0].style.transform = '';
      spans[1].style.opacity = '';
      spans[2].style.transform = '';
    }
  });
  
  // Close mobile menu when clicking outside
  document.addEventListener('click', function(e) {
    if (!navToggle.contains(e.target) && !navLinks.contains(e.target)) {
      navLinks.classList.remove('active');
      navToggle.classList.remove('active');
      const spans = navToggle.querySelectorAll('span');
      spans[0].style.transform = '';
      spans[1].style.opacity = '';
      spans[2].style.transform = '';
    }
  });
  
  // Close mobile menu when clicking a link
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('active');
      navToggle.classList.remove('active');
      const spans = navToggle.querySelectorAll('span');
      spans[0].style.transform = '';
      spans[1].style.opacity = '';
      spans[2].style.transform = '';
    });
  });
}

// ===========================
// Header Scroll Effect
// ===========================
let lastScroll = 0;
window.addEventListener('scroll', function() {
  const currentScroll = window.pageYOffset;
  
  // Add scrolled class for header styling
  if (currentScroll > 50) {
    header.classList.add('scrolled');
  } else {
    header.classList.remove('scrolled');
  }
  
  // Hide/show header on scroll
  if (currentScroll > lastScroll && currentScroll > 100) {
    header.style.transform = 'translateY(-100%)';
  } else {
    header.style.transform = 'translateY(0)';
  }
  
  lastScroll = currentScroll;
});

// ===========================
// Intersection Observer for Animations
// ===========================
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      
      // Animate children with stagger
      const children = entry.target.querySelectorAll('.feature-card, .collab-card');
      children.forEach((child, index) => {
        setTimeout(() => {
          child.style.opacity = '1';
          child.style.transform = 'translateY(0)';
        }, index * 100);
      });
    }
  });
}, observerOptions);

// Observe sections
document.querySelectorAll('.features-row, .collaborations-grid').forEach(section => {
  observer.observe(section);
});

// Special observer for collaborations content
if (collaborationsContent) {
  const collabObserver = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        collabObserver.disconnect();
      }
    });
  }, { threshold: 0.3 });
  
  collabObserver.observe(collaborationsContent);
}

// ===========================
// Smooth Scroll for Anchor Links
// ===========================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      const headerOffset = 80;
      const elementPosition = target.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
      
      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });
    }
  });
});

// ===========================
// Logo Slider Enhancement
// ===========================
const sliderTrack = document.querySelector('.slider-track');
if (sliderTrack) {
  // Pause animation on hover
  sliderTrack.addEventListener('mouseenter', () => {
    sliderTrack.style.animationPlayState = 'paused';
  });
  
  sliderTrack.addEventListener('mouseleave', () => {
    sliderTrack.style.animationPlayState = 'running';
  });
}

// ===========================
// Initialize Animation States
// ===========================
document.addEventListener('DOMContentLoaded', function() {
  // Set initial states for animated elements
  document.querySelectorAll('.feature-card, .collab-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(30px)';
    card.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
  });
  
  // Add loading animation to hero
  const heroContent = document.querySelector('.hero .content');
  if (heroContent) {
    heroContent.style.opacity = '0';
    setTimeout(() => {
      heroContent.style.opacity = '1';
      heroContent.style.transition = 'opacity 1s ease';
    }, 100);
  }
});

// ===========================
// Performance Optimization
// ===========================
let ticking = false;
function requestTick() {
  if (!ticking) {
    window.requestAnimationFrame(updateElements);
    ticking = true;
  }
}

function updateElements() {
  ticking = false;
  // Add any scroll-based animations here
}

// Debounced resize handler
let resizeTimer;
window.addEventListener('resize', function() {
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(function() {
    // Handle resize events
    console.log('Window resized');
  }, 250);
});