$(document).ready(function(){
  $("img").addClass("animated slideInDown");
  $("a").click(function() {
    $("#credits").addClass("animated hinge");
  });
});

$(".disc").hover(function () {
  $(".disc").addClass("animated rubberBand");
});

$("#web").hover(function () {
  $("#web").addClass("animated rubberBand");
});
