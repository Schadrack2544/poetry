
  const maxLength = 50;
  const text = document.querySelector('.miniText').textContent;
  const trimmedText = text.substring(0, maxLength) + (text.length > maxLength ? '...' : '');
  document.querySelector('.miniText').textContent = trimmedText;

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

  $(document).ready(function() {
    var currentIndex = 0;
    var images = $('.featured-image img');
    var maxIndex = images.length - 1;
  
    // show the first image
    images.eq(currentIndex).addClass('active');
  
    // handle the next button click
    $('.next-btn').click(function() {
      images.eq(currentIndex).removeClass('active');
  
      if (currentIndex === maxIndex) {
        currentIndex = 0;
      } else {
        currentIndex++;
      }
  
      images.eq(currentIndex).addClass('active');
    });
  
    // handle the prev button click
    $('.prev-btn').click(function() {
      images.eq(currentIndex).removeClass('active');
  
      if (currentIndex === 0) {
        currentIndex = maxIndex;
      } else {
        currentIndex--;
      }
  
      images.eq(currentIndex).addClass('active');
    });
  });
  