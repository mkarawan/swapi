document.getElementById('goback').addEventListener('click', () => {
  history.back();
});

function showHide(index) {
  var div = document.getElementById('more'+index);
  if (div.style.display === 'none'){
    div.style.display = 'block';
  }
  else {
    div.style.display = "none";
  }
}