$.get('https://swapi-api.hbtn.io/api/films/?format=json',
  function (data) {
    var result = data.results;
    for (let i = 0; i < result.length; i++) { 
	var name = result[i].title;
	var tmp = "<li>" + name + "</li>";
	$('ul#list_movies').append(tmp);
    }
  });
