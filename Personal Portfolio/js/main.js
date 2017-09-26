$(window).scroll(function() {
  if ($(this).scrollTop() <= 950) {
    $('#wrapper').addClass('colorOne')
      .removeClass('colorTwo');
  } else if ($(this).scrollTop() <= 1600) {
    $('#wrapper').addClass('colorTwo')
      .removeClass('colorThree');
  } else if ($(this).scrollTop() <= 1700) {
    $('#wrapper').addClass('colorThree')
      .removeClass('colorFour');
  }  else {
    $('#wrapper').addClass('colorOne')
  }
});
