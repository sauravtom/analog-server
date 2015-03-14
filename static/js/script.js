

$( "#send" ).click(function() {
  msg = $('#msg').val();
  console.log(msg);
  $(".commentArea").append( "<div class='bubbledRight'>"+msg+"</div>" );
  resp = "foo";
  $(".commentArea").append( "<div class='bubbledLeft'>"+resp+"</div>" );
});

$("#msg").keyup(function (e) {
    if (e.keyCode == 13) {
        // Do something
        msg = $('#msg').val();
        $('#msg').val(""); 
        console.log(msg);
        $(".commentArea").append( "<div class='bubbledRight'>"+msg+"</div>" );

        var min = 2, max = 4;
        var delay = Math.floor(Math.random() * (max - min) + min) * 1000;
        var dots="";
        setTimeout(
          function() {
          	$(".commentArea").append( "<div class='bubbledLeft typing'>typing</div>" );
          	
          	window.setInterval(function(){
          	  n=Math.floor(new Date().getTime() / 1000)%10%4;
          	  for(i=0;i<n;i++){dots+=".";}
          	  $(".typing").html( "typing"+dots );
          	  dots="";
          	}, 1000);
            
          }, delay);

        dots="";
        var min = 4, max = 15;
        var delay = Math.floor(Math.random() * (max - min) + min) * 1000;
        setTimeout(
          function() {
            var resp = "Hi Saurav, wassup !!";
            $(".typing").hide();
            $(".commentArea").append( "<div class='bubbledLeft'>"+resp+"</div>" );
          }, delay);
    }
});