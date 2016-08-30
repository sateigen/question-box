var $questionID = $('.question')[0].id
var $answerAnchor = $('#answer_anchor')

function displayAnswers(answers, anchor) {
  answers.forEach(function(answer) {
    var $panel = $('<div>').addClass("panel panel-default").appendTo(anchor)
    var $desc = $('<div>').addClass("panel-body").text(answer.description).appendTo($panel)
    var $foot = $('<div>').addClass("panel-footer").text("submitted: " + Date(answer.created_on) + " by " + answer.user).appendTo($panel)
  })
}


$.ajax({ url:'/api/answer/', data: {question: $questionID} }).done(function(response) {
  displayAnswers(response.results, $answerAnchor)
})
