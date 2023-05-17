
  // const maxLength = 50;
  // const text = document.querySelector('.miniText').textContent;
  // const trimmedText = text.substring(0, maxLength) + (text.length > maxLength ? '...' : '');
  // document.querySelector('.miniText').textContent = trimmedText;
  const menuIcon = document.querySelector('.menu-icon');
  const menuEls = document.querySelector('.menu-els');

menuIcon.addEventListener('click', function() {
  // this.parentElement.classList.toggle('responsive');
  menuEls.classList.toggle('responsive');
  
});

  // get the header element
const header = document.querySelector('.menu');

// get the offset top of the header element
//const headerOffsetTop = header.offsetTop;

// add an event listener to the window object to listen for scroll events
window.addEventListener('scroll', function() {
 
  // if the window has been scrolled past the offset top of the header element,
  // add the 'fixed' class to the header element; otherwise, remove it
  if (window.pageYOffset >= 20) {
    header.classList.add('fixed');
  } else {
    header.classList.remove('fixed');
  }
});
