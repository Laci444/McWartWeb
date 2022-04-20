document.querySelectorAll('a').forEach(element => {
    element.addEventListener('click', function(e) {
      e.preventDefault();
      alert('Ez egy demo változat. A linkek nem működnek!');
    });
  });
  document.querySelectorAll('input').forEach(element => {
    element.addEventListener('click', function(e) {
      e.preventDefault();
      alert('Ez egy demo változat. A linkek nem működnek!');
    });
  });