// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

if($('.question').length >= 1) {
  var $questionID = $('.question')[0].id
}

var $answerAnchor = $('#answer_anchor')
var $addAnswer = $('#add_answer')
var $activeUser = $("#userName")[0].value
var $finalAnswer = $("#final_answer")
var $newQuestion = $('#new_question')
var $saveQuestion = $('#saveQuestion')


$saveQuestion.click(function(){
  console.log("YES")
  var $title = $("#questionTitle")[0].value
  var $desc = $("#questionDescription")[0].value
  $.ajax({url:'/api/question/',
          method:'POST',
          data: {'title': $title, 'description': $desc, 'score': 0, 'user': $activeUser},
          success: function(){
            console.log("WOW")
            $('#myModal').hide()
          }});
})

function displayAnswers(answers, anchor) {
  answers.forEach(function(answer) {
    var $panel = $('<div>').addClass("panel panel-default").appendTo(anchor)
    var $desc = $('<div>').addClass("panel-body").text(answer.description).appendTo($panel)
    var $foot = $('<div>').addClass("panel-footer").text("submitted: " + Date(answer.created_on) + " by " + getUsername(answer.user)).appendTo($panel)
  })
}

// This function should get the username for the answerer/commenter, but it doesn't
function getUsername(userid) {
  $.ajax({ url:'/api/user/', data: {id: userid} }).done(function(response) {
    console.log(response.results[0].username)
    return response.results[0].username
  })
}

$.ajax({ url:'/api/answer/', data: {question: $questionID} }).done(function(response) {
  displayAnswers(response.results, $answerAnchor)
})


$finalAnswer.on("submit",function(e){
  e.preventDefault();
  console.log("step one")
  var $newAnswer = $('#newAnswer')[0].value
  $.ajax({
    type:'POST',
    url:'/api/answer/',
    data: {'user': $activeUser, 'score': 0, 'description': $newAnswer, 'question': $questionID},
    success: function() { window.location.reload(true)},
    error: function(e) {
      console.log(e)
    }
  })
})
