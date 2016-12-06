$('.carousel--full').slick({
  arrows: false,
  autoplay: true,
  autoplaySpeed: 2000,
  centerMode: true,
  centerPadding: '200px',
  cssEase: "linear",
  slidesToScroll: 1,
  slidesToShow: 4,

  responsive: [{
    breakpoint: 1700,
    settings: {
      slidesToShow: 3,
      centerPadding: '100px'
    }
  }, {
    breakpoint: 1024,
    settings: {
      slidesToShow: 2,
      centerPadding: '50px'
    }
  }, {
    breakpoint: 700,
    settings: {
      slidesToShow: 1,
      centerPadding: '25px'
    }
  }]
});