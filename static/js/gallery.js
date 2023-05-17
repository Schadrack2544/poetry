
// $(document).ready(function() {
    let modal = document.getElementById('modal');
    let modalImage = document.getElementById('modalImage');
    let galleryImages = document.querySelectorAll('.featured-images img');
    
    let slideIndex = 0;
    
    function openModal(img) {
      modal.style.display = 'block';
      modalImage.src = img.src;
      slideIndex = Array.from(galleryImages).indexOf(img);
    }
    
    function closeModal() {
      modal.style.display = 'none';
    }
    
    function plusSlides(n) {
      slideIndex += n;
      if (slideIndex < 0) {
        slideIndex = galleryImages.length - 1;
      }
      if (slideIndex >= galleryImages.length) {
        slideIndex = 0;
      }
      modalImage.src = galleryImages[slideIndex].src;
    }
    
    document.addEventListener('keydown', function(event) {
      if (event.key === 'ArrowLeft') {
        plusSlides(-1);
      }
      if (event.key === 'ArrowRight') {
        plusSlides(1);
      }
    });
    
//   });
  