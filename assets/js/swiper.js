new Swiper('.swiper', {
    speed: 1000,
    loop: true,
    autoplay: {
      delay: 3000,
      disableOnInteraction: false
    }
    ,pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
    ,navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      }
    ,scrollbar: {
        el: '.swiper-scrollbar',
      },

  });