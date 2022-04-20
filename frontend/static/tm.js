$('#timeback').click(function () {
    // animate content
    $('#container').addClass('animate_content');
    $('.row').fadeOut(100);
  
    setTimeout(function () {
      window.location.replace('/wayback');
    }, 1400);
  
  
  });
  