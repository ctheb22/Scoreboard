
$(function() {
	const game_id = JSON.parse(document.getElementById('game').gameId);
  /////////////////////INPUT HANDLERS///////////////////////////////
	/////////TITLE////////////////
  $('#title_form').on('submit', function(event){
      event.preventDefault();
      console.log("title form submitted!")  // sanity check
      set_title($(#title_input).val());
  });

	/////////HOME TEAM////////////
	$('#home_name_form').on('submit', function(event){
      event.preventDefault();
      console.log("home team name submitted!")  // sanity check
      set_name('home', $('#home_name').val());
  });
	
	$('#home_plus_seven').on('click', function(event){
      event.preventDefault();
      console.log("Home + 7 clicked!")  // sanity check
      update_score('home', '+', 7);
  });
	
	$('#home_sub_seven').on('click', function(event){
      event.preventDefault();
      console.log("Home - 7 clicked!")  // sanity check
      update_score('home', '-', 7);
  });
	
	$('#home_plus_three').on('click', function(event){
      event.preventDefault();
      console.log("Home + 3 clicked!")  // sanity check
      update_score('home', '+', 3);
  });
	
	$('#home_sub_three').on('click', function(event){
      event.preventDefault();
      console.log("Home - 3 clicked!")  // sanity check
      update_score('home', '-', 3);
  });
	
	$('#home_score_form').on('submit', function(event){
      event.preventDefault();
      console.log("home score submitted!")  // sanity check
      update_score('home', '=', $('#home_score').val());
  });
	
	///////AWAY TEAM/////////////////
	$('#away_name_form').on('submit', function(event){
      event.preventDefault();
      console.log("Away team submitted!")  // sanity check
      set_name('away', $('#away_name').val);
  });
	
	$('#away_plus_seven').on('click', function(event){
      event.preventDefault();
      console.log("Away + 7 clicked!")  // sanity check
      update_score('away', '+', 7);
  });
	
	$('#away_sub_seven').on('click', function(event){
      event.preventDefault();
      console.log("Away - 7 clicked!")  // sanity check
      update_score('away', '-', 7);
  });
	
	$('#away_plus_three').on('click', function(event){
      event.preventDefault();
      console.log("Away + 3 clicked!")  // sanity check
      update_score('away', '+', 3);
  });
	
	$('#away_sub_three').on('click', function(event){
      event.preventDefault();
      console.log("Away - 3 clicked!")  // sanity check
      update_score('away', '-', 3);
  });
	
	$('#away_score_form').on('submit', function(event){
      event.preventDefault();
      console.log("Away score form submitted!")  // sanity check
      update_score('away', '=', $('#away_score').val());
  });
	
	//////////TIME/////////////////
	$('#time_form').on('submit', function(event){
      event.preventDefault();
      console.log("time form submitted!")  // sanity check
			//Get seconds from form input.
      update_time('=', get_seconds_from_form($('#time_input').val()));
  });
	
	$('#time_plus_five').on('click', function(event){
      event.preventDefault();
      console.log("Time + 5 clicked!")  // sanity check
      update_time('+', 5);
  });
	
	$('#time_sub_five').on('click', function(event){
      event.preventDefault();
      console.log("Time - 5 clicked!")  // sanity check
      update_time('-', 5);
  });
	
	$('#time_plus_one').on('click', function(event){
      event.preventDefault();
      console.log("Time + 1 clicked!")  // sanity check
      update_time('+', 1);
  });
	
	$('#time_sub_one').on('click', function(event){
      event.preventDefault();
      console.log("Time - 1 clicked!")  // sanity check
      update_time('-', 1);
  });
	
	/////////QUARTER///////////////
	$('#quarter_form').on('submit', function(event){
      event.preventDefault();
      console.log("quarter form submitted!")  // sanity check
      update_quarter('=', $(#quarter_input).val());
  });
	
	$('#quarter_plus_one').on('click', function(event){
      event.preventDefault();
      console.log("Quarter + 1 clicked!")  // sanity check
      update_quarter('+', 1);
  });
	
	$('#quarter_sub_one').on('click', function(event){
      event.preventDefault();
      console.log("Quarter - 1 clicked!")  // sanity check
      update_quarter('-', 1);
  });
	
	//////////DOWN/////////////////
	$('#down_form').on('submit', function(event){
      event.preventDefault();
      console.log("Down form submitted!")  // sanity check
      update_down('=', $(#down_input).val());
  });
	
	$('#down_plus_one').on('click', function(event){
      event.preventDefault();
      console.log("Down + 1 clicked!")  // sanity check
      update_down('+', 1);
  });
	
	$('#down_sub_one').on('click', function(event){
      event.preventDefault();
      console.log("Down - 1 clicked!")  // sanity check
      update_down('-', 1);
  });
	
	/////////BLURB////////////////
	$('#blurb_form').on('submit', function(event){
      event.preventDefault();
      console.log("Blurb form submitted!")  // sanity check
      update_blurb(cleanse_text_input($('#blurb_input_area').val()));
  });


	////////AJAX FUNCTIONS///////

	function set_title(title_val) {
		console.log("Set Title")
		$.ajax({
			url : game_id+"/"+setTitle,
			type : "POST",
			data : {'title' : title_val},
			
			success : function(json){
				update_interface(json)
			},
			
			error : function(xhr,errmsg,err){
				//set the results box with the error. Probably needed
				//to differentiate between error locations.
			}
	}

	function set_name(team, name) {
		console.log("Set Name")
		$.ajax({
			url : game_id+"/"+team+"/"+name,
			type : "POST",
			data : {},
			
			success : function(json){
				update_interface(json)
			},
			
			error : function(xhr,errmsg,err){
				//set the results box with the error. Probably needed
				//to differentiate between error locations.
			}
	}
	
	function update_score(team, op, score) {
		console.log("Update Score")
		if (isNaN(score)) 
		{
			alert("Must input number for score.");
			return false;
		}
		$.ajax({
			url : game_id+"/"+team+"/"+op+score,
			type : "POST",
			data : {},
			
			success : function(json){
				update_interface(json)
			},
			
			error : function(xhr,errmsg,err){
				//set the results box with the error. Probably needed
				//to differentiate between error locations.
			}
	}
	
	function update_time(op, time) {
		console.log("Update Time")
		if (isNaN(time)) 
		{
			alert("Must input number for time.");
			return false;
		}
		$.ajax({
			url : game_id+"/time/"+op+time,
			type : "POST",
			data : {},
			
			success : function(json){
				update_interface(json)
			},
			
			error : function(xhr,errmsg,err){
				//set the results box with the error. Probably needed
				//to differentiate between error locations.
			}
	}
	
	function update_quarter(op, quarter) {
		console.log("Update Quarter")
		if (isNaN(quarter)) 
		{
			alert("Must input number for quarter.");
			return false;
		}
		$.ajax({
			url : game_id+"/quarter/"+op+quarter,
			type : "POST",
			data : {},
			
			success : function(json){
				update_interface(json)
			},
			
			error : function(xhr,errmsg,err){
				//set the results box with the error. Probably needed
				//to differentiate between error locations.
			}
	}
	
	function update_down(op, down) {
		console.log("Update Down.")
		if (isNaN(down)) 
		{
			alert("Must input number for down.");
			return false;
		}
		$.ajax({
			url : game_id+"/down/"+op+down,
			type : "POST",
			data : {},
			
			success : function(json){
				update_interface(json)
			},
			
			error : function(xhr,errmsg,err){
				//set the results box with the error. Probably needed
				//to differentiate between error locations.
			}
	}
	
	function update_blurb(blurb_value) {
		console.log("Update Blurb.")
		$.ajax({
			url : game_id+"/setBlurb",
			type : "POST",
			data : {'blurb': blurb_value},
			
			success : function(json){
				update_interface(json)
			},
			
			error : function(xhr,errmsg,err){
				//set the results box with the error. Probably needed
				//to differentiate between error locations.
			}
	}
	
	
  function create_post() {
    console.log("create post is working!") // sanity check
    $.ajax({
        url : "create_post/", // the endpoint
        type : "POST", // http method
        data : { the_post : $('#post-text').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#post-text').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
  };
	
	////////UTILITY FUNCTIONS////
	function get_seconds_from_form(time){
		return time;
	}
	
	function cleanse_text_input(text){
		return text;
	}
	
	function update_interface(json){
		//json has {"type" : type, "data" : data}
	}
	
	
///////////////////////////AJAX TOKEN CRUFT////////////////////////////////

  // This function gets cookie with a given name
  function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie != '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) == (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');

  /*
  The functions below will create a header with csrftoken
  */

  function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  function sameOrigin(url) {
      // test that a given url is a same-origin URL
      // url could be relative or scheme relative or absolute
      var host = document.location.host; // host + port
      var protocol = document.location.protocol;
      var sr_origin = '//' + host;
      var origin = protocol + sr_origin;
      // Allow absolute or scheme relative URLs to same origin
      return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
          (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
          // or any other URL that isn't scheme relative or absolute i.e relative.
          !(/^(\/\/|http:|https:).*/.test(url));
  }

  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
              // Send the token to same-origin, relative URLs only.
              // Send the token only if the method warrants CSRF protection
              // Using the CSRFToken value acquired earlier
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });

});
