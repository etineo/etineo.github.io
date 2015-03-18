$(document).ready(function(){
  var card_array = ["fishie", "fishie", "turtle", "turtle", "piggie", "piggie", "doggie", "doggie", "kitty", "kitty", "sssnake", "sssnake", "birdie", "birdie", "goat", "goat", "hamster", "hamster", "dragon", "dragon"]

  for(i in card_array){
    $('#card_holder').append('<div class="card"><p>'+card_array[i]+'</p></div>');
  }

	var card1 = '0';
  var card2 = '0';
  var click_count = 'first';
	$('.card').on('click' function() {
    if(click_count == 'first'){
 	 		$mycard=$(this).find('p');
 	 		$mycard.css('opacity',1);
 	 		card1=$mycard.html();
      click_count = 'second';
    }
    else{ 
      $mycard=$(this).find('p');
 	 		$mycard.css('opacity',1);
 	 		card1=$mycard.html();
      
    }
	})
});





