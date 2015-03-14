

$( "#send" ).click(function() {
  msg = $('#msg').val();
  console.log(msg);
  $(".commentArea").append( "<div class='bubbledRight'>"+msg+"</div>" );
  resp = "foo";
  $(".commentArea").append( "<div class='bubbledLeft'>"+resp+"</div>" );
});