
  const maxLength = 50;
  const text = document.querySelector('.miniText').textContent;
  const trimmedText = text.substring(0, maxLength) + (text.length > maxLength ? '...' : '');
  document.querySelector('.miniText').textContent = trimmedText;

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
  