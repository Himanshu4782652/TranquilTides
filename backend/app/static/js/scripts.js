// scripts.js

document.addEventListener('DOMContentLoaded', () => {
 // Example: Smooth scroll for internal links
 const links = document.querySelectorAll('nav a');

 links.forEach(link => {
  link.addEventListener('click', function (e) {
   e.preventDefault();
   const targetId = this.getAttribute('href').substring(1);
   const targetElement = document.getElementById(targetId);

   if (targetElement) {
    targetElement.scrollIntoView({
     behavior: 'smooth',
     block: 'start'
    });
   }
  });
 });
});
