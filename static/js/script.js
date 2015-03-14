

string_ = "Hey how has been your day so far :). ! How are you feeling right now. ! I am bored, talk to me please :/!\
What has been the most significant thing that happened to you today ? ! Type a message to talk to me.".split('!');

window.setInterval(function(){
			  var dots="";
          	  n=Math.floor(new Date().getTime() / 1000)%10%4;
          	  for(i=0;i<n;i++){dots+=".";}
          	  $(".typing").html( "typing"+dots );
          	  dots="";
          	}, 1000);

var rnd_msg = string_[Math.floor(Math.random()*string_.length)];
$(".commentArea").append( "<div class='bubbledLeft'>"+rnd_msg+"</div>" );

$("#msg").keyup(function (e) {
    if (e.keyCode == 13) {
        // Do something
        msg = $('#msg').val();
        if (msg == "") return;
        $('#msg').val(""); 

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
          	$.get( "/message?msg="+msg, function( data ) {
          	  //console.log( data );
          	  var resp = data;
          	  $(".typing").hide();
          	  $(".commentArea").append( "<div class='bubbledLeft'>"+resp+"</div>" );
          	});
            
          }, delay);
    }
});